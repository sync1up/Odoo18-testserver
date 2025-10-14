import json, requests
from odoo import http
from odoo.http import request

OPENAI_PARAM_KEY = "openai.api_key"
DEFAULT_MODEL = "gpt-4o-mini"

class OpenAIChatController(http.Controller):

    @http.route("/openai/chat", type="json", auth="user")
    def chat(self, message, model=DEFAULT_MODEL):
        sess = request.env["openai.chat.session"].sudo().get_or_create_for_user(request.env.user)
        sess.append_message("user", message)

        api_key = request.env["ir.config_parameter"].sudo().get_param(OPENAI_PARAM_KEY)
        if not api_key:
            return {"error": "Missing OpenAI API key. Set system parameter 'openai.api_key'."}

        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {"model": model, "messages": json.loads(sess.messages or "[]")}

        try:
            r = requests.post("https://api.openai.com/v1/chat/completions",
                              headers=headers, json=payload, timeout=45)
        except requests.RequestException as e:
            return {"error": f"OpenAI request failed: {e}"}

        if r.status_code >= 400:
            return {"error": f"OpenAI error {r.status_code}: {r.text[:800]}"}

        data = r.json()
        content = (data.get("choices") or [{}])[0].get("message", {}).get("content", "")
        if not content:
            return {"error": "Empty response from OpenAI."}

        sess.append_message("assistant", content)
        return {"reply": content}

    @http.route("/openai/history", type="json", auth="user")
    def history(self):
        sess = request.env["openai.chat.session"].sudo().get_or_create_for_user(request.env.user)
        return {"messages": json.loads(sess.messages or "[]")}

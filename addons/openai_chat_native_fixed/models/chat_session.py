from odoo import api, fields, models
import json

class OpenAIChatSession(models.Model):
    _name = "openai.chat.session"
    _description = "Per-user OpenAI chat session"
    _rec_name = "user_id"
    _order = "write_date desc"
    _sql_constraints = [
        ("unique_user", "unique(user_id)", "Each user can have only one OpenAI chat session."),
    ]

    user_id = fields.Many2one("res.users", required=True, default=lambda self: self.env.user, index=True)
    messages = fields.Text(default="[]")
    create_date = fields.Datetime(readonly=True)
    write_date = fields.Datetime(readonly=True)

    @api.model
    def get_or_create_for_user(self, user):
        rec = self.sudo().search([("user_id", "=", user.id)], limit=1)
        if not rec:
            rec = self.sudo().create({"user_id": user.id})
        return rec

    def append_message(self, role, content):
        self.ensure_one()
        try:
            msgs = json.loads(self.messages or "[]")
        except Exception:
            msgs = []
        msgs.append({"role": role, "content": content})
        self.sudo().write({"messages": json.dumps(msgs)})
        return msgs

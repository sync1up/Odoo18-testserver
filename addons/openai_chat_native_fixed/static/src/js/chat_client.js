/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, onMounted, useState, xml } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";

class OpenAIChatClient extends Component {
    setup() {
        this.state = useState({ messages: [], sending: false, input: "" });
        onMounted(async () => {
            const hist = await jsonrpc("/openai/history", {});
            this.state.messages = hist.messages || [];
            this.render();
        });
    }
    async send() {
        const text = (this.state.input || "").trim();
        if (!text || this.state.sending) return;
        this.state.sending = true;
        this.state.messages.push({ role: "user", content: text });
        this.state.input = "";
        this.render();
        try {
            const res = await jsonrpc("/openai/chat", { message: text });
            if (res.error) {
                this.state.messages.push({ role: "assistant", content: "⚠️ " + res.error });
            } else {
                this.state.messages.push({ role: "assistant", content: res.reply });
            }
        } finally {
            this.state.sending = false;
            this.render();
        }
    }
}
OpenAIChatClient.template = xml`
<div class="o_content oa-root">
  <div class="oa-wrap">
    <div class="oa-chat-box">
      <t t-foreach="state.messages" t-as="m" t-key="m">
        <div t-attf-class="oa-msg {{ m.role }}">
          <div class="oa-bubble"><t t-esc="m.content"/></div>
        </div>
      </t>
    </div>
    <div class="oa-input">
      <input type="text" t-model="state.input" placeholder="Stel je vraag..." class="oa-text"/>
      <button t-on-click="send" t-att-disabled="state.sending" class="oa-send">Verstuur</button>
    </div>
  </div>
</div>`;
registry.category("actions").add("openai_chat_native.client", OpenAIChatClient);

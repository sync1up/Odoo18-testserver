# -*- coding: utf-8 -*-
import subprocess
import os
import logging
from odoo import models, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# Check of PyQt6 beschikbaar is
try:
    import PyQt6
    PYQT_AVAILABLE = True
except ImportError:
    _logger.warning("PyQt6 not installed. Please run: pip3 install PyQt6 PyQt6-WebEngine")
    PYQT_AVAILABLE = False


class ChatGPTLauncher(models.TransientModel):
    _name = 'chatgpt.launcher'
    _description = 'ChatGPT Browser Launcher'

    @api.model
    def launch_browser(self):
        """Launch ChatGPT browser voor huidige gebruiker"""
        if not PYQT_AVAILABLE:
            raise UserError(
                "PyQt6 is not installed on this system.\n\n"
                "Please ask your system administrator to run:\n"
                "pip3 install PyQt6 PyQt6-WebEngine"
            )

        user_id = self.env.user.id
        user_name = self.env.user.name

        _logger.info(f"Launching ChatGPT browser for user: {user_name} (ID: {user_id})")


        module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        browser_script = os.path.join(module_path, 'bin', 'chatgpt_browser.py')

        if not os.path.exists(browser_script):
            raise UserError(f"ChatGPT browser script not found at: {browser_script}")

        try:
            python_executable = 'python3'
            subprocess.Popen(
                [python_executable, browser_script, '--user', str(user_id)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                start_new_session=True
            )

            _logger.info(f"ChatGPT browser successfully launched for user {user_id}")

            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'ChatGPT Browser',
                    'message': 'ChatGPT browser window wordt geopend...',
                    'type': 'success',
                    'sticky': False,
                }
            }

        except Exception as e:
            _logger.error(f"Failed to launch ChatGPT browser: {str(e)}")
            raise UserError(f"Could not launch ChatGPT browser: {str(e)}")

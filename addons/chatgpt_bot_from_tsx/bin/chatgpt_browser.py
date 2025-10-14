#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ChatGPT Browser Window
Standalone PyQt6 browser voor ChatGPT
"""
import sys
import argparse
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


class ChatGPTBrowser(QMainWindow):
    def __init__(self, user_id=None):
        super().__init__()
        self.user_id = user_id
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f'ChatGPT Browser - User {self.user_id}')
        self.setGeometry(100, 100, 1200, 800)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://chat.openai.com'))
        self.setCentralWidget(self.browser)
        self.show()


def main():
    parser = argparse.ArgumentParser(description='ChatGPT Browser')
    parser.add_argument('--user', type=str, help='User ID', default='unknown')
    args = parser.parse_args()
    app = QApplication(sys.argv)
    app.setApplicationName('ChatGPT Browser')
    browser = ChatGPTBrowser(user_id=args.user)
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

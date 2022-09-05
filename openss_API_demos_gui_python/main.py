import sys
import json

import requests
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import LoginFormUI, MainMenuUI
from api_demos import alignment, detect, face_compare, pose

TOKEN_URL = "http://eco-open.study.sensetime.com/api/common/v1/token"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.access_key = ""
        self.access_secret = ""
        # Bandaid fix for double click
        self.runningDemo = False
        self.loadLoginMenu()
        #self.ui.exitButton.clicked.connect(exit_application(self))

    def center(self):
        qr = self.frameGeometry()
        cp = QWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # overridden
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    # overridden
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def verifyKeys(self, key_id, key_secret):
        # For testing purposes, remove if still here by launch
        if (key_id == "override"):
            self.access_key, self.access_secret = "PQT7s9q3sWUJkXho", "m3Jw2qq0AwGtNZo8ZvfezpZeJAvGpgZE"
            self.loadMainMenu()
            return "random"

        headers = {"languageType": "en"}
        token_params = {"accessKeyId": key_id, "accessKeySecret": key_secret}
        token_response = requests.get(url=TOKEN_URL, headers=headers, params=token_params, verify=False).text
        token = json.loads(token_response).get("data")
        if token is not None:
            self.access_key, self.access_secret = key_id, key_secret
            self.loadMainMenu()
        return token

    def loadMainMenu(self):
        self.ui = MainMenuUI.Ui_MainWindow()
        self.ui.setupUi(self)

    def loadLoginMenu(self):
        self.ui = LoginFormUI.Ui_MainWindow()
        self.ui.setupUi(self)

    def loadAPIDemo(self, demo_type):
        # Switch case not available on python3.8
        # Reimplement as enum or switch case when available
        if self.runningDemo == False:
            if demo_type == "alignment":
                self.runningDemo = True
                self.runningDemo = alignment.main(ACCESS_KEY_ID=self.access_key, ACCESS_KEY_SECRET=self.access_secret)
            elif demo_type == "detect":
                self.runningDemo = True
                self.runningDemo = detect.main(ACCESS_KEY_ID=self.access_key, ACCESS_KEY_SECRET=self.access_secret)
            elif demo_type == "compare":
                self.runningDemo = True
                self.runningDemo = face_compare.main(ACCESS_KEY_ID=self.access_key, ACCESS_KEY_SECRET=self.access_secret)
            elif demo_type == "pose":
                self.runningDemo = True
                self.runningDemo = pose.main(ACCESS_KEY_ID=self.access_key, ACCESS_KEY_SECRET=self.access_secret)
            else:
                print("No such demo")
        else:
            print("Already running a demo")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
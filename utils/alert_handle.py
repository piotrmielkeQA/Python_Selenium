from selenium.webdriver.common.alert import Alert


class AlertHandle():

    def __init__(self):
        self.driver = None

    def accept_alert(self):
        Alert(self.driver).accept()

    def dismiss_alert(self):
        Alert(self.driver).dismiss()

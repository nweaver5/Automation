class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

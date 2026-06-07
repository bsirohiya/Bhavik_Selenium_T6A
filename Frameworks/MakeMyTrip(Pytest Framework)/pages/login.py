from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    googleFrame = (By.XPATH, '//iframe')
    google = (By.XPATH, '//div[@aria-labelledby="button-label"]')
    username = (By.XPATH, '//li[@class="aZvCDf ZRzegd W7Aapd zpCp3 SmR8"]')

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_google_iframe(self):
        self.switch_to_iframe(self.googleFrame)

    def click_google(self):
        self.click(self.google)

    def switch_to_google_window(self):
        self.switch_to_new_window()

    def click_account(self):
        self.click(self.account)




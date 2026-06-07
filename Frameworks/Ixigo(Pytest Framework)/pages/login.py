from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    cancelBtn = (By.XPATH, '//button[@id="closeButton"]')
    loginBtn = (By.XPATH, '(//button[contains(. , "Log in")])[1]')
    iframe = (By.XPATH, '//iframe[@title="Sign in with Google Button"]')
    signin = (By.XPATH, '//span[text()="Sign in with Google"]')
    email = (By.XPATH, '//input[@type="email"]')
    next = (By.XPATH, '//span[.="Next"]')
    password = (By.XPATH, '//input[@type="password"]')

    def __init__(self, driver):
        super().__init__(driver)

    def action_chains(self):
        self.action_chain()

    def click_login(self):
        self.click(self.loginBtn)

    def switch_to_google_iframe(self):
        self.switch_to_iframe(self.iframe)

    def click_loginBtn(self):
        self.click(self.signin)

    def switch_to_google_window(self):
        self.switch_to_new_window()

    def send_email(self, email):
        self.enter_text(self.email, email)

    def click_next(self):
        self.click(self.next)

    def enter_password(self, password):
        self.enter_text(self.password, password)



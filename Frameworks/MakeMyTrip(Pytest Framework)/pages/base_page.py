from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def hover_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def scroll_to(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.scroll_to_element(element).perform()

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_iframe(self, locator):
        iframe = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.switch_to.frame(iframe)
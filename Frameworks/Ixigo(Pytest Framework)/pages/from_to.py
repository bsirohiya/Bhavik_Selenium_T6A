from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class From_to_Page(BasePage):

    fromPlace = (By.XPATH, '(//div[@class="flex-1 h-full flex flex-col justify-center px-15 py-10 "])[1]')
    fromCity = (By.XPATH, '(//div[@role="listitem"])[14]')
    fromCityInput = (By.XPATH, '(//input[contains(@class, "outline-none w-full bg-transparent placeholder:text-disabled pt-3")])[1]')
    # toPlace = (By.XPATH, '(//div[@class="flex justify-between items-center relative w-full h-full pl-10 block"])[2]')
    toCity = (By.XPATH, '(//input[contains(@class, "outline-none")])[2]')
    toCityInput = (By.XPATH, '(//div[@role="listitem"])[24]')
    date = (By.XPATH, '(//button[@type="button"])[28]')
    adults = (By.XPATH, '(//button[@data-testid="4"])[1]')
    done = (By.XPATH, '//button[.="Done"]')
    search = (By.XPATH, '//button[.="Search"]')

    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_new_window_back_logged(self):
        self.switch_to_new_window_back()

    def click_from(self):
        self.click(self.fromPlace)

    def enter_from_city(self, fromCityInput):
        self.enter_text(self.fromCityInput, fromCityInput)

    def click_from_city(self):
        self.click(self.fromCity)

    def enter_to_city(self, toCity):
        self.enter_text(self.toCity, toCity)

    def click_to_city(self):
        self.click(self.toCityInput)

    def click_date(self):
        self.click(self.date)

    def click_adults(self):
        self.click(self.adults)

    def click_done(self):
        self.click(self.done)

    def click_search(self):
        self.click(self.search)

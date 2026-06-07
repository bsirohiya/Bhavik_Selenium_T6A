from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MenSneakers(BasePage):

    men = (By.XPATH, '//a[.="Men"]')
    sneakers = (By.XPATH, '//a[.="Sneakers"]')

    ankle_height = (By.XPATH, '(//h4[@class="atsa-title"])[1]')
    mid_top = (By.XPATH, '//ul[@class="atsa-values"]/descendant::label[2]')
    materials = (By.XPATH, '(//h4[@class="atsa-title"])[6]')
    canvas = (By.XPATH, '//ul[@class="atsa-values"]/descendant::label[1]')
    product = (By.XPATH, '//ul[@class="results-base"]/li[19]')
    # product = (By.XPATH, '(//ul[@class="results-base"]/descendant::h3[.="BERSACHE"])[3]')

    size = (By.XPATH, '//div[@class="size-buttons-size-buttons"]/descendant::button[4]')
    add_to_bag = (By.XPATH, '//div[.="ADD TO BAG"]')

    def __init__(self,driver):
        super().__init__(driver)

    def hover_to_men(self):
        self.hover_to(self.men)

    def click_sneakers(self):
        self.click(self.sneakers)

    def click_ankle_height(self):
        self.click(self.ankle_height)

    def click_mid_top(self):
        self.click(self.mid_top)

    def click_materials(self):
        self.click(self.materials)

    def click_canvas(self):
        self.click(self.canvas)

    def scroll_to_product(self):
        self.scroll_to(self.product)

    def click_product(self):
        self.click(self.product)

    def switch_to_product_page(self):
        self.switch_to_new_window()

    def select_size(self):
        self.click(self.size)

    def add_to_cart(self):
        self.click(self.add_to_bag)
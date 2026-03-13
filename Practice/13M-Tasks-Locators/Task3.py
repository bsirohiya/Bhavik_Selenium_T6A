'''
 Using ID and PARTIAL LINK TEXT
--> Open Amazon
--> Search for Mobiles (use ID)
--> Click on any 1 mobile (use PARTIAL LINK TEXT)
'''

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://amazon.in/")
sleep(2)

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "iPhone 16 Plus").click()




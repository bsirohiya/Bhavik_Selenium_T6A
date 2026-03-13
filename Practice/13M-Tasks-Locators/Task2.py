'''
 Using Name
--> Open Facebook
--> Enter email and password
'''

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.maximize_window()

driver.get("https://www.facebook.com")

driver.find_element(By.ID, "_R_1h6kqsqppb6amH1_").send_keys("Ram")
driver.find_element(By.ID, "_R_1hmkqsqppb6amH1_").send_keys("Ram@1234")

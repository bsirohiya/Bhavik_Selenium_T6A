'''

'''

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.wikipedia.com")
driver.refresh()
print(driver.title)

driver.get("https://www.amazon.in/")
print(driver.title)
sleep(5)
driver.back()
sleep(5)
driver.close()

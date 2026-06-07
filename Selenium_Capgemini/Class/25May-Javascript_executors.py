from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions() # o is the object of this class
o.add_experimental_option("detach", True) # We make browser to be open for infinite time not for blink
driver = Chrome(options=o)

driver.get('https://amazon.in')
driver.maximize_window()
sleep(2)
# driver.execute_script("window.scrollTo(0,1000)")
# sleep(2)
# driver.execute_script("window.scrollBy(0,500)")
# sleep(2)
# driver.execute_script("window.scrollBy(0,500)")

ele = driver.find_element(By.XPATH, '(//span[@class="a-list-item"])[3]')

driver.execute_script("arguments[0].scrollIntoView(false)", ele) # false - element at bottom of page

driver.execute_script("arguments[0].scrollIntoView(true)", ele) # true - element at top of page

sleep(2)

# driver.quit()
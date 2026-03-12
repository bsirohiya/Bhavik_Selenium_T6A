'''from time import sleep
from selenium.webdriver import Chrome
driver = Chrome()
sleep(5) '''
from time import sleep

'''from -> Keyword
selenium -> package
webdriver -> module
Chrome and ChromeOptions -> Class
driver -> Variable which is holding browser'''

from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions() # o is the object of this class
o.add_experimental_option("detach", True) # We make browser to be open for infinite time not for blink
driver = Chrome(options=o)


# To open a webpage
driver.get('https://amazon.in/')  # get return type is none

# # To maximize window
# driver.maximize_window()
# sleep(2)
#
# # To minimize window
# driver.minimize_window()
# sleep(2)

# Fullscreen
# driver.fullscreen_window()

# To fetch the title of tab
print(driver.title)

# Fetch URL
print(driver.current_url)

# Page Source code
# print(driver.page_source)

# Browser name
print(driver.name)

driver.maximize_window()

sleep(5)
# driver.close() # Only that 1 tab gets closed and remaining tab remains open
# driver.quit() # It will close entire browser window with all tabs

driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()


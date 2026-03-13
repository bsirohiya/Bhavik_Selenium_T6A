'''
There are two method to find the element /s:
                1. find_element(locator_name,locator_value) ->
                                -> Single element
                                -> returns one single web element
                                -> for error "No such element exception"

                2. find_elements(locator_name,locator_value) ->
                                -> Multiple elements
                                -> returns list of web elements
                                -> for error "Empty list"

types of locators ->

DIRECT LOCATOR
1. ID
2. NAME
3. CLASSNAME
4. TAG NAME

TEXT BASED
5. LINK TEXT
6. PARTIAL LINK TEXT

EXPRESSION BASED
7. CSS SELECTOR
8. X PATH

Element Actions
1. click()
2. send_keys('text')
'''

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

# driver.get("https://demoqa.com/text-box")

'''
# 1. Locator - ID
driver.get("https://demoqa.com/text-box")

driver.maximize_window()
# sleep(5)
driver.find_element(By.ID, "userName").send_keys("hehehe")
driver.find_element(By.ID, "userEmail").send_keys("hahaha")
driver.find_element(By.ID, "currentAddress").send_keys("Here only")
driver.find_element(By.ID, "permanentAddress").send_keys("Here only 2.0")

driver.find_element(By.ID, "submit").click()'''

'''
#  1. ID - Amazon input field locator
driver.get("https://amazon.com")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shirts")
driver.find_element(By.ID, "nav-search-submit-button").click()'''


# # 2. NAME
# driver.find_element(By.NAME, "field-keywords").send_keys("shirts")
# driver.find_element(By.ID, "search").send_keys("shirts")


# 3. CLASS_NAME
# driver.get("https://amazon.com")
# driver.find_element(By.CLASS_NAME, "nav-input.nav-progressive-attribute").send_keys("shirts")


# 4. TAG NAME
# driver.find_element(By.TAG_NAME, "input").send_keys("helloo")


# 5. LINK TEXT
# driver.get("https://amazon.in/")
# sleep(2)
# driver.find_element(By.LINK_TEXT,"Mobiles").click()


# 6. PARTIAL LINK TEXT
# driver.get("https://amazon.in/")
# sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT, "Mob").click()


# 7. CSS SElECTORS - tagname[attribute = "value]
driver.get("https://amazon.in/")
sleep(2)
driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search Amazon.in"]').send_keys("shirt")



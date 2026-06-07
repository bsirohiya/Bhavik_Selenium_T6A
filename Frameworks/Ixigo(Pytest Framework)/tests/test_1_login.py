from time import sleep

from config.env import ConfigReader
from pages.login import LoginPage


def test_login(setup_and_teardown):
    driver = setup_and_teardown

    config = ConfigReader.read_config()
    env = config['qa']
    username = env['username']
    password = env['password']
    lp = LoginPage(driver)

    sleep(3)
    lp.action_chains()
    sleep(2)
    lp.click_login()
    sleep(2)
    lp.switch_to_google_iframe()
    sleep(2)
    lp.click_loginBtn()
    sleep(2)
    lp.switch_to_google_window()
    sleep(2)
    lp.send_email(username)
    sleep(2)
    lp.click_next()
    sleep(2)
    lp.enter_password(password)
    sleep(2)
    lp.click_next()
    sleep(2)

    # assert driver.status_code == 302


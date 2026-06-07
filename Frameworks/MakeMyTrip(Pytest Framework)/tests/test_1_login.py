from pages.login import LoginPage

def test_login(setup_and_teardown):
    driver = setup_and_teardown

    lp = LoginPage(driver)
    lp.switch_to_google_iframe()
    lp.click_google()
    lp.switch_to_google_window()
    lp.click_account()
from time import sleep

from pages.from_to import From_to_Page


def test_from_to(setup_and_teardown):
    driver = setup_and_teardown

    ft = From_to_Page(driver)

    sleep(2)
    ft.switch_to_new_window_back_logged()
    # sleep(3)
    # ft.action_chain()
    sleep(2)
    ft.click_from()
    sleep(2)
    ft.enter_from_city("jaipur")
    sleep(2)
    ft.click_from_city()
    sleep(2)
    ft.enter_to_city("delhi")
    sleep(2)
    ft.click_to_city()
    sleep(2)
    ft.click_date()
    sleep(2)
    ft.click_adults()
    sleep(2)
    ft.click_done()
    sleep(2)
    ft.click_search()
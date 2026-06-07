from cmath import polar
from time import sleep

from pages.men_sneakers import MenSneakers

def test_men_sneakers(setup_and_teardown):

    driver = setup_and_teardown

    ms = MenSneakers(driver)

    ms.hover_to_men()
    ms.click_sneakers()
    # sleep(2)
    ms.click_ankle_height()
#     sleep(2)
    ms.click_mid_top()
#     sleep(2)
    ms.click_materials()
#     sleep(2)
    ms.click_canvas()
#     sleep(2)
    ms.scroll_to_product()
#     sleep(2)
    ms.click_product()
    ms.switch_to_product_page()

    ms.select_size()
    ms.add_to_cart()

    assert driver.status_code == 200, "Error"

# huehue
# helppppp meee!!!
# thankyou so much for saving me
# while unsaved ppl:
    # save polar
    # unsaved ppl=unsaved ppl-1
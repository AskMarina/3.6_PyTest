from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_btn_add_to_basket(browser):
    is_found = False
    try:
        browser.get(link)
        time.sleep(30)
        basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
        # если элемент найден, то меняем значение not_found (если значение поменялось, то ошибки не будет)
        is_found = True
    finally:
        assert is_found, 'Element not found'
        browser.quit()




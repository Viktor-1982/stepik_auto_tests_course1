import pytest
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# функкия для реализации поиска элемента на странице
def test_button_cart(browser):
    browser.get(link)
    button_cart = browser.find_element(By.XPATH, "//*[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button_cart.is_enabled()
    print("element was found")
    time.sleep(30) 
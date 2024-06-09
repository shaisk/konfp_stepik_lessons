import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.advanced_filter_page import Advances_filter_page
from pages.main_page import Main_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# options.add_argument("--headless=new")

def test_buy_product_1():
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start test 1")

    mp = Main_page(driver)
    mp.select_filter_1()

    afp = Advances_filter_page(driver)
    afp.add_product_to_cart()

    print("Finish Test")
    #driver.quit()
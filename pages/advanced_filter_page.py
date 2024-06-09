from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base


class Advances_filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_1_buy_button = "//*[@id='content']/div/div[2]/div[1]/div[5]/div/div[2]/a"
    product_add_to_cart_text = "/html/div/div/div[2]"
    cart_button = "//a[@class='link-to-cart']"

    # Getters

    def get_product_1_buy_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1_buy_button)))

    def get_product_add_to_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_add_to_cart_text)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    # Actions

    def click_product_1_buy_button(self):
        self.get_product_1_buy_button().click()
        print("Product 1 get to the cart")

    def click_get_cart_button(self):
        self.get_cart_button().click()
        print("Select cart")

    # Methods

    def add_product_to_cart(self):
        self.get_current_url()
        self.click_product_1_buy_button()
        self.assert_word(self.get_product_add_to_cart_text().text, 'ТОВАР ДОБАВЛЕН В КОРЗИНУ')
        self.click_get_cart_button()

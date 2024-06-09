import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart_text = "//*[@id='breadcrumbs']"
    product_text = "//*[@id='cart_product_row2124']/td[2]/a"
    edit_quantity = "//*[@id='cart_product_row2124']/td[4]/input"
    remove_from_cart_button = "//*[@id='cart_product_row2124']/td[6]/div"
    empty_cart_text = "//*[@id='content']/div"

    # Getters

    def get_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_text)))

    def get_product_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_text)))

    def get_edit_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.edit_quantity)))

    def get_remove_from_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.remove_from_cart_button)))

    def get_empty_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart_text)))

    # Actions

    def edit_edit_quantity(self):
        self.get_edit_quantity().clear()
        self.get_edit_quantity().send_keys('4')
        print("Edit quantity of product")

    def click_remove_from_cart_button(self):
        self.get_remove_from_cart_button().click()
        print("Product 1 removed from the cart")

    # Methods

    def actions_with_the_product(self):
        self.get_current_url()
        self.assert_word(self.get_cart_text().text, 'Корзина')
        self.assert_word(self.get_product_text().text, 'СЮЖЕТ (900г)')
        self.edit_edit_quantity()
        self.click_remove_from_cart_button()
        time.sleep(5)
        self.assert_word(self.get_empty_cart_text().text, 'Корзина пуста')

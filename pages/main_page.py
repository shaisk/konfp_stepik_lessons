from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from base.base_class import Base


class Main_page(Base):

    url = 'https://konf-p.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)
        self.driver = driver

    # Locators

    filter_cardboard = "//*[@id='paramFilter']/form/div/div[1]/div[2]/div[1]/label"
    filter_height_from = "//*[@id='paramFilter']/form/div/div[2]/div[2]/div[1]/div/span[1]"
    filter_height_to = "//*[@id='paramFilter']/form/div/div[2]/div[2]/div[1]/div/span[2]"
    choose_gifts_button = "//*[@id='paramFilter']/form/div/div[3]/div[1]"

    # Getters

    def get_filter_cardboard(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_cardboard)))

    def get_filter_height_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_height_from)))

    def get_filter_height_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_height_to)))

    def get_choose_gifts_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_gifts_button)))

    # Actions

    def click_filter_cardboard(self):
        self.get_filter_cardboard().click()
        print("Select filter cardboard")

    def click_and_hold_select_filter_height_from(self):
        self.action.click_and_hold(self.get_filter_height_from()).move_by_offset(40, 0).release().perform()
        print("Filter height from success")

    def click_and_hold_select_filter_height_to(self):
        self.action.click_and_hold(self.get_filter_height_to()).move_by_offset(xoffset=-40, yoffset=0).release().perform()
        print("Filter height to success")

    def click_choose_gifts_button(self):
        self.get_choose_gifts_button().click()
        print("Click to choose gifts button")

    # Methods

    def select_filter_1(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_filter_cardboard()
        self.click_and_hold_select_filter_height_from()
        self.click_and_hold_select_filter_height_to()
        self.click_choose_gifts_button()

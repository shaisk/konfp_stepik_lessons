from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    url = 'https://konf-p.ru'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


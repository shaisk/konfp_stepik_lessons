class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method GET current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")
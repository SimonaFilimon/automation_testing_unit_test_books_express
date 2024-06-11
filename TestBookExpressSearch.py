import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class TestBookExpressSearch(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.books-express.ro/")
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
    def tearDown(self):
        self.driver.quit()
    def test_search_product_cauta_The_DC_Book(self):
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("the dc book")
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.ENTER)
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_product_deschide_carte(self):
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("the dc book2")
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[src='https://i3.books-express.ro/bt/9780241506431/the-dc-book.jpg']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_product_adauga_in_cos(self):
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("the dc book1")
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "[src='https://i3.books-express.ro/bt/9780241506431/the-dc-book.jpg']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class ='add2cart danger button full icon']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_product_autentificare(self):
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("the dc book2")
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "[src='https://i3.books-express.ro/bt/9780241506431/the-dc-book.jpg']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class ='button success']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_product_introduce_email(self):
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("the dc book")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[src='https://i3.books-express.ro/bt/9780241506431/the-dc-book.jpg']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class ='button success']").click()
        self.driver.find_element(By.XPATH, "//input['email']").send_keys("test.@test.t")
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input['email']").send_keys(Keys.ENTER)
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
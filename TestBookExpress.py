import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBookExpress(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.books-express.ro/")
    def tearDown(self):
        self.driver.quit()
    def test_search_product_sectiune(self):
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_top(self):
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_autor(self):
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "Seth Godin").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_relevanta(self):
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "Seth Godin").click()
        self.driver.find_element(By.LINK_TEXT, "Relevanță").click()
        self.driver.find_element(By.LINK_TEXT, "Data publicării").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_autor2(self):
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "The Kpi Institute").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
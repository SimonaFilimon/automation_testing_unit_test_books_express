import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class TestBookExpress(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.books-express.ro/")
        self.driver.find_element(By.ID, "cookieconsent:desc").click()
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
    def tearDown(self):
        self.driver.quit()
    def test_search_product_sectiune(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_topvanzari(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_autorSethGodin(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        self.driver.find_element(By.LINK_TEXT, "Seth Godin").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_relevanta(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari")
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Relevanță").click()
        self.driver.find_element(By.LINK_TEXT, "Data publicării").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
    def test_search_products_TheKpiInstitute(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='category-menu']").click()
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Top vanzari2")
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.XPATH, "//input[@name='q']").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "The Kpi Institute").click()
        assert len(self.driver.find_elements(By.CLASS_NAME, "polipop__notifications")) == 2
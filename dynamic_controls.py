from lib2to3.pgen2 import driver
from msilib.schema import CheckBox
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Dynamic Controls").click()

    def test_dynamic_controls(self):
        driver = self.driver

        checkBox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkBox.click()

        remove_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector("#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > input[type=text]")))

        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.send_keys('Platzi')
        
        enable_disable_button.click()


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
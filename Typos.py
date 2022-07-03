from lib2to3.pgen2 import driver
from pickle import TRUE
import unittest
from selenium import webdriver


class Typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Typos").click()

    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_ckeck =  paragraph_to_check.text
        print(text_to_ckeck)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_ckeck != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_ckeck =  paragraph_to_check.text
            driver.refresh()


        while found:
            if text_to_ckeck == correct_text:
                tries += 1
                driver.refresh()
                found = True
        
        self.assertEqual(found, True)

        print(f"it took {tries} tries to find the typo")


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
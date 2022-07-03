import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from time import sleep


class Chrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.google.com/')

    def test_Ingress(self):
        driver = self.driver

        ingresar = driver.find_element_by_name('q')
        ingresar.clear()
        ingresar.send_keys("Mercado Libre")
        ingresar.submit()
        sleep(3)

        ingresar1 = driver.find_element_by_partial_link_text('Mercado Libre Colombia - Envíos Gratis en el día')
        ingresar1.click()
        sleep(3)


        ingresar2 = driver.find_element_by_class_name('nav-search-input')
        ingresar2.clear()
        ingresar2.send_keys("Patineta")
        ingresar2.submit()
        sleep(3)

        ingresar3 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/button[1]')
        ingresar3.click()
        sleep(4)
        


        location = driver.find_element_by_partial_link_text('Bogotá D.C.')
        location.click()
        sleep(3)

        Condition = driver.find_element_by_partial_link_text('Nuevo')
        Condition.click()
        sleep(4)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output = 'reportesChrome', report_name = 'Chrome'))
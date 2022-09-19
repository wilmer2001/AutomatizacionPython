import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUp(cls):
        #self.driver = webdriver.Chrome(executable_path= r'C:\Users\wilmer\Documents\Automatizacion\chromedriver_win32')
        cls.driver = webdriver.Chrome(executable_path= r'./chromedriver_win32/chromedriver.exe')  
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
       # driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        #self.driver.get('https://wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

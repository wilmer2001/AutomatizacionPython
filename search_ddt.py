import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    @data(('dress',6), ('music', 5))
    @unpack


    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_fiel = driver.find_element_by_name('q')
        search_fiel.clear()
        search_fiel.send_keys(search_value)
        search_fiel.submit()

        products = driver.find_element_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))


    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main(verbosity= 2)
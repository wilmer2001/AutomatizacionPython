import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= './chromedriver_win32/chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        element_added = int(input('How many elements will you add?: '))
        element_removed = int(input('How many elements will you remove?: '))
        total_elements = element_added - element_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

        sleep(3)

        for i in range(element_added):
            add_button.click()

        for i in range(element_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click
            except:
                print(f"You're trying to delet more elements the the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("there 0 are elements on screen")

        sleep(3)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)
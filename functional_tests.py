import unittest
from selenium import webdriver

class ResourcesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.localServer = 'http://127.0.0.1:8000'

    def tearDown(self):
        self.driver.quit()
        pass

    def test_home_page(self):
        self.driver.get(self.localServer)
        self.assertIn('Szwagier Mikrus Server', self.driver.title)
        resources_link = self.driver.find_element_by_id("id_resources_home")
        resources_link.click()
        self.assertIn('Produkty', self.driver.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

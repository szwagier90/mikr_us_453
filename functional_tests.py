import unittest
from selenium import webdriver

class ResourcesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn('Produkty', self.driver.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

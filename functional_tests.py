import unittest
from selenium import webdriver

class ServerPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get('http://127.0.0.1:8000')
        self.assertIn('Szwagier Mikrus Server', self.driver.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

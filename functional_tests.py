import unittest
from selenium import webdriver

class ResourcesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.localServer = 'http://127.0.0.1:8000'

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get(self.localServer)
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main()

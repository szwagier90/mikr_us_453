import unittest
from selenium import webdriver

class ResourcesPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Django', self.browser.title)


if __name__ == '__main__':
    unittest.main()

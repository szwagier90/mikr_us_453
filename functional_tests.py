import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class ServerPage(unittest.TestCase):
    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=firefox_options)
        self.localServer = 'http://127.0.0.1:8000'

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get(self.localServer)
        self.assertIn('Szwagier Mikrus Server', self.driver.title)

        home_header = self.driver.find_element_by_tag_name("h1").text
        self.assertEqual("Szwagier Mikrus Server", home_header)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

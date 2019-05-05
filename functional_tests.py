import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class ResourcesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.localServer = 'http://127.0.0.1:8000'

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get(self.localServer)
        self.assertIn('Szwagier Mikrus Server', self.driver.title)

        home_header = self.driver.find_element_by_tag_name("h1").text
        self.assertEqual("Szwagier Mikrus Server", home_header)

        self.driver.find_element_by_id("id_dev_srv_link")

        resources_page_link = self.driver.find_element_by_id("id_resources_home")
        self.assertEqual("Produkty", resources_page_link.text)
        resources_page_link.click()

        self.assertEqual("Produkty", self.driver.title)
        resources_header = self.driver.find_element_by_tag_name("h1").text
        self.assertEqual("Produkty", resources_header)

        product_input = self.driver.find_element_by_id("id_input_product")
        self.assertEqual(
            product_input.get_attribute('placeholder'),
            "Wpisz nazwę produktu",
        )
        product_input.send_keys("Pomidory Krojone")
        product_input.send_keys(Keys.ENTER)

        time.sleep(1)

        products_table = self.driver.find_element_by_id("id_products_table")
        products_rows = products_table.find_elements_by_tag_name("tr")
        self.assertIn("Pomidory Krojone", [row.text for row in products_rows])


if __name__ == '__main__':
    unittest.main()

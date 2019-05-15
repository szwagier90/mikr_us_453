from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

import time

MAX_WAIT = 10

class ResourcesPage(LiveServerTestCase):
    def wait_for_row_in_products_table(self, product):
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element_by_id("id_products_table")
                rows = table.find_elements_by_tag_name("td")
                self.assertIn(product, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.2)

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get(self.live_server_url)
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

        self.wait_for_row_in_products_table("Pomidory Krojone")

        product_input = self.driver.find_element_by_id("id_input_product")
        self.assertEqual(
            product_input.get_attribute('placeholder'),
            "Wpisz nazwę produktu",
        )
        product_input.send_keys("Banan")
        product_input.send_keys(Keys.ENTER)

        self.wait_for_row_in_products_table("Pomidory Krojone")
        self.wait_for_row_in_products_table("Banan")

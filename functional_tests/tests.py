from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import time

MAX_WAIT = 10


class ServerPage(LiveServerTestCase):
    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=firefox_options)

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get(self.live_server_url)
        self.assertIn('Szwagier Mikrus Server', self.driver.title)

        home_header = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Szwagier Mikrus Server", home_header)


class TasksPage(LiveServerTestCase):
    def setUp(self):
        self.firefox_options = Options()
        self.firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.firefox_options)

    def tearDown(self):
        self.driver.quit()

    def wait_for_row_in_task_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.driver.find_element(By.ID, 'id_task_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_home_page(self):
        self.driver.get(self.live_server_url)
        self.assertIn('Szwagier Mikrus Server', self.driver.title)

        tasks_page_link = self.driver.find_element(By.ID, "id_tasks_home")
        self.assertEqual("Zadania", tasks_page_link.text)

        tasks_page_link.click()
        self.assertIn('Task management site', self.driver.title)

        header_text = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("Task", header_text)

        taskbox = self.driver.find_element(By.ID, 'id_new_task')
        self.assertEqual(
            taskbox.get_attribute('placeholder'),
            'New task: '
        )

        taskbox.send_keys('Order contact lenses')
        taskbox.send_keys(Keys.ENTER)
        time.sleep(1)

        taskbox = self.driver.find_element(By.ID, 'id_new_task')
        taskbox.send_keys('Visit eye doctor')
        taskbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.wait_for_row_in_task_table('Order contact lenses')
        self.wait_for_row_in_task_table('Visit eye doctor')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.driver.get(self.live_server_url+'/tasks')
        taskbox = self.driver.find_element(By.ID, 'id_new_task')
        taskbox.send_keys('Order contact lenses')
        taskbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_task_table('Order contact lenses')

        first_task_list_url = self.driver.current_url
        self.assertRegex(first_task_list_url, '/tasks/.+')

        self.driver.quit()
        self.driver = webdriver.Firefox(options=self.firefox_options)

        self.driver.get(self.live_server_url+'/tasks')
        page_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Order contact lenses', page_text)
        self.assertNotIn('Visit eye doctor', page_text)

        taskbox = self.driver.find_element(By.ID, 'id_new_task')
        taskbox.send_keys('Check engine')
        taskbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_task_table('Order contact lenses')

        second_task_list_url = self.driver.current_url
        self.assertRegex(second_task_list_url, '/tasks/.+')
        self.assertNotEqual(first_task_list_url, second_task_list_url)

        page_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Order contact lenses', page_text)
        self.assertIn('Check engine', page_text)

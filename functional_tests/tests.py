from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

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
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=firefox_options)

    def tearDown(self):
        self.driver.quit()

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

        self.fail('Finish the test!')

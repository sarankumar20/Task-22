# using python selenium automation and the url https://www.instagram.com/guviofficial/ kindly do the following mentioned in the task
# 1.use either relative or absolute xpath only for the task
# 2.extract the total numbers of following and followers from the url mentioned above

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException

class Instagram:
    def __init__(self, link):
        self.web_url = link
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        # Create a new WebDriver instance
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def insta_home_page(self):
        # getting url and open in browser
        self.driver.get(self.web_url)
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//button[@class="_abn5 _abn6 _aa5h"]/span').click()

    def get_information(self):
        try:
           #  we can get title and current url of webpage
           title_webpage = self.driver.title
           print(f'title of page:{title_webpage}')
           curr_url = self.driver.current_url
           print(curr_url)
        except NoSuchAttributeException as error_2:
            print(error_2)

    def get_data(self):
        try:
            # in this element using relative xpath to get all the text
            items =self.driver.find_elements(by=By.XPATH, value='//span[@class="_ac2a"]')
            for a in items:
                print(a.text)
        except NoSuchElementException as error_1:
            print(error_1)
    def follower(self):
        try:
            # in this element using relative xpath to get all the text
            total_count_follower = self.driver.find_element(by=By.XPATH, value='//button[text()=" followers"]')
            print(f'Total followers are :{total_count_follower.text}')
        except NoSuchElementException as error_1:
            print(error_1)
    def following(self):
        try:
            # in this element using relative xpath to get all the text
            total_count_following = self.driver.find_element(by=By.XPATH,value='//button[text()=" following"]')
            print(f'Total count followings are: {total_count_following.text}')
        except NoSuchElementException as error_1:
            print(error_1)
        finally:
            self.driver.close()

url = "https://www.instagram.com/guviofficial/"
data = Instagram(url)
data.insta_home_page()
data.get_information()
data.get_data()
data.follower()
data.following()
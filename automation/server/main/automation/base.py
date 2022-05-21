from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Base:

    def __init__(self, PATH, url, headless=False):

        chrome_options = Options()

        if headless:
            chrome_options.set_headless()

        self.driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
        self.driver.get(url)
        self.driver.maximize_window()
        self.name_field = None

        time.sleep(3)

    def findByName(self, name):
        print('find element by name ...')
        self.name_field = self.driver.find_element(by=By.NAME, value=name)
        return True

    # def find_by_tag_name(self, name: str) -> bool:
    #     self.driver.find_element(By.TAG_NAME, name)
    #
    def findByTextAreas(self, name):
        print('find textArea ...')
        xpath = f"//textarea"
        self.name_field = self.driver.find_element(by=By.XPATH, value=xpath)
        return True

    def findByTypeEmail(self, name):
        print('find by type email ...')
        xpath = f"//input[@type='email']"
        self.name_field = self.driver.find_element(by=By.XPATH, value=xpath)
        return True

    def findByNameEmail(self, name):
        print('find by type email ...')
        xpath = f"//input[contains(@name, 'email')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=xpath)
        return True

    def findByNameEmailCapitalize(self, name):
        print('find by type email Capitalize ...')
        xpath = f"//input[contains(@name, 'Email')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=xpath)
        return True

    def findById(self, name):
        print('find element by id ...')
        self.name_field = self.driver.find_element(by=By.ID, value=name)
        return True

    def searchByNameString(self, name):
        print('find element by name string ...')
        place_holder_xpath = f"//*[contains(@name, '{name}')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=place_holder_xpath)
        return True

    def searchByNameStringCapitalized(self, name):
        print('find element by name string capitalized ...')
        place_holder_xpath = f"//*[contains(@name, '{name.capitalize()}')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=place_holder_xpath)
        return True

    def searchByNameStringUpperCase(self, name):
        print('find element by name string upper ...')
        place_holder_xpath = f"//*[contains(@name, '{name.upper()}')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=place_holder_xpath)
        return True

    def searchByPlaceholder(self, name):
        print('find element by placeholder ...')
        place_holder_xpath = f"//*[contains(@placeholder, '{name}')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=place_holder_xpath)
        return True

    def searchByPlaceholderCapitalized(self, name):
        print('find element by placeholder capitalized ...')
        place_holder_xpath = f"//*[contains(@placeholder, '{name.capitalize()}')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=place_holder_xpath)
        return True

    def searchByPlaceholderUpperCase(self, name):
        print('find element by placeholder upper ...')
        place_holder_xpath = f"//*[contains(@placeholder, '{name.upper()}')]"
        self.name_field = self.driver.find_element(by=By.XPATH, value=place_holder_xpath)
        return True

    def findById(self, name):
        print('find element by id ...')
        xpath = f"//input[contains(@id, '{name.upper()}')]"
        self.name_field = self.driver.find_element(by=By.ID, value=name)
        return True

    def findByIdCapitalize(self, name):
        print('find element by id capitalize...')
        xpath = f"//input[contains(@id, '{name.upper()}')]"
        self.name_field = self.driver.find_element(by=By.ID, value=name.capitalize())
        return True

    def submit_btn(self):
        button = self.driver.find_element(by=By.XPATH, value="//input[@type='submit']")
        button.click()

        # name.send_keys(Keys.RETURN)

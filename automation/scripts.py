import random

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.main.automation.base import Base


class AutomateForm(Base):

    def waitForTitle(self):
        xpath = "//title"
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
            print(e)

    def find_and_set_field(self, name, value, alt_name):

        present = False
        # element_func = [self.findByName, self.findById, self.searchByPlaceholder]
        element_search_func = [
            self.findByName,
            self.searchByPlaceholder,
            self.searchByPlaceholderCapitalized,
            self.searchByPlaceholderUpperCase,
            self.searchByNameString,
            self.searchByNameStringCapitalized,
            self.searchByNameStringUpperCase,
            self.findById,
            self.findByIdCapitalize
        ]

        # find field by name, label, placeholder
        for elem in element_search_func:
            try:
                if elem(name):
                    present = True
                    break
            except Exception as e:
                print(e)

        # if element was found/exist
        if present and self.name_field is not None:
            self.name_field.send_keys(value)

    def find_email_and_set_field(self, value, alt_name):

        present = False
        element_search_func = [
            self.findByName,
            self.searchByPlaceholder,
            self.searchByPlaceholderCapitalized,
            self.findByTypeEmail,
            self.findByNameEmail,
            self.findByNameEmailCapitalize,
            self.findById,
            self.findByIdCapitalize
        ]

        # find field by name, label, placeholder
        for elem in element_search_func:
            try:
                if elem('email'):
                    present = True
                    break
            except Exception as e:
                print(e)

        # if element was found/ exist
        if present and self.name_field is not None:
            self.name_field.send_keys(value)

    def find_message_box_and_set_field(self, value, alt_name):
        names = ['message', 'comments', 'questions']
        present = False
        # element_func = [self.findByName, self.findById, self.searchByPlaceholder]
        element_search_func = [
            self.searchByPlaceholder,
            self.searchByPlaceholderCapitalized,
            self.searchByPlaceholderUpperCase,
            self.findByTextAreas,
            self.searchByNameString,
            self.searchByNameStringCapitalized,
            self.searchByNameStringUpperCase,
        ]

        # find field by name, label, placeholder
        for name in names:
            for elem in element_search_func:
                try:
                    if elem(name):
                        present = True
                        break
                except Exception as e:
                    print(e)

        # if element was found/ exist
        if present and self.name_field is not None:
            self.name_field.send_keys(value)

    def find_empty_inputs_and_set_value(self, values=["Sam", "vwede", "wisdow", "dev-pro"]):
        try:
            empty_inputs = self.driver.find_elements(By.XPATH, "//form//input")
            empty_inputs_count = 0
            print(f"found {len(empty_inputs)} inputs")
            for field in empty_inputs:
                if field.get_attribute("type") not in ["hidden", "Hidden", "HIDDEN"]:
                    value = field.get_attribute("value")
                    if value == "":
                        print('shuffling values ...')
                        random.shuffle(values)
                        empty_inputs_count += 1
                        field.clear()
                        field.send_keys(values.pop())

            print(f"{len(empty_inputs_count)} empty inputs has been pre filled")

        except Exception as err:
            print(err)

    def select_value_in_select_box(self):
        try:
            for _select in self.driver.find_elements(By.TAG_NAME, 'select'):
                Select(_select).select_by_index(1)
        except Exception as err:
            print(err)

    def check_input_boxes(self):
        try:
            checks, counts = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']"), 0
            for check in checks:
                if counts == 1:
                    break       # Avoid clicking all checkbox but just 1
                check.click()
                counts += 1
        except Exception as err:
            print(err)

    def radio_input_boxes(self):
        for radio in self.driver.find_elements(By.XPATH, "//input[@type='radio']"):
            radio.click()

    def solve_text_captcha(self):
        pass

    def solve_robot_captcha(self):
        pass


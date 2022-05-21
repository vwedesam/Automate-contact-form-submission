import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base import Base


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

    def find_messaage_box_and_set_field(self, value, alt_name):

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

    def set_other_text_fields(self):
        pass

    def select_value_in_selectBox(self):
        get_all_select_tags = self.driver.find_elements(By.TAG_NAME, 'select')
        for _select in get_all_select_tags:
            _ = Select(_select).select_by_index(1)

    def check_input_boxes(self):
        pass

    def radio_input_boxes(self):
        pass

    def solve_text_captcha(self):
        pass

    def solve_robot_captcha(self):
        pass


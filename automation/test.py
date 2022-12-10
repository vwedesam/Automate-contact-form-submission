import time
import os
from scripts import AutomateForm
import unittest

PATH = "./chromedriver"

url = os.getenv('FORM_URL') or "http://localhost:5000"


class TestAutomateContactForm(unittest.TestCase):

    def setUp(self):
        self.firstname = 'Nwa'
        self.lastname = 'wisdom'
        self.phone = "+234080000000"
        self.email = "sam@gmail.com"
        self.other = "others"
        self.message = "message, text, quest comment"

        self.form = AutomateForm(PATH, url)

        self.form.waitForTitle()

    def test_preFillInputs(self):

        self.form.find_and_set_field('name', f"{self.lastname} {self.firstname}", '_email')

        self.form.find_and_set_field('first', f"{self.firstname}", '_email')

        self.form.find_and_set_field('last', f"{self.lastname}", '_email')

        self.form.find_and_set_field('phone', self.phone, '_phone')

        self.form.find_email_and_set_field(self.email, '_email')

        self.form.find_message_box_and_set_field(self.message, '_message')

        self.form.select_value_in_select_box()

        self.form.check_input_boxes()

        self.form.radio_input_boxes()

        self.form.find_empty_inputs_and_set_value()

        time.sleep(100)


if __name__ == '__main__':
    unittest.main()

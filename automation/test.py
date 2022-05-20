from server.main.automation.script import AutomateForm


PATH = "./chromedriver.exe"
url = "https://www.mni.net/contact/"

form = AutomateForm(PATH, url)


form.find_and_set_field('email', 'crypticologist@gmail.com', '_email')

form.find_and_set_field('fullname', 'wisdom Oga', 'full_name')

form.find_and_set_field('firstname', 'wisdom', 'first_name')

form.find_and_set_field('lastname', 'Oga', 'last_name')



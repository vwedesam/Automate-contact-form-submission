import time

from server.main.automation.script import AutomateForm


PATH = "./chromedriver"

# url = "https://www.mni.net/contact/"
# url = "http://aerenoutsourcing.com/contact-us.html"
# url = "https://www.nacsllc.org/contact"
# url = "https://hoar.com/contact-alabama/"
# url = "https://www.cefatradetraining.org/contact/" #re-visit
# url = "https://www.beckumlaw.com/contact-us.html"
# url = "https://www.boealabama.com/pages/resources/contact.php"
# url = "https://brookstonerestoration.com/contact-us/"
# url = "https://caddell.com/contact-us/" # re visit
# url = "https://calldixie.com/contact/" # select
# url = "https://www.bidnet.com/contact-us" # re-visit
# url = "https://www.islandpestcontrol.net/"
# url = "https://business.manufacturealabama.org/contact/" #re-visit
# url = "https://www.tyonek.com/contact-us/"
# url = "https://pittstrailers.com/contact-us/" #captcha
# url = "https://www.ncralaska.com/contact-us" #captcha
# url = "https://www.alaska.co.nz/contact-us"
url = "https://www.graniteconstruction.com/company/contact-us" #re-visit
# url = "https://alaskastructures.com/contacts/" #re-visit
# url = "https://www.hccontractors.net/contact/" # re-visit -captcha -- and form
# url = "https://www.drakeconstruction.net/contact-us/" #re-visit
# url = "https://www.associatedmetalcast.com/contact/"


# business.etowahchamber.org/list/member/honda-manufacturing-of-alabama-llc-6822
# re-visit
# https://www.briceenvironmental.com/contact-us/
# https://www.tbi-construction.com/contact-us/
# https://uicalaska.com/contact-us/office-contacts-and-locations/
# https://www.shapecorp.com/contactform/
# https://www.horiba.com/int/contact/contact-form/
# https://www.phillipsmfg.com/contact-phillips/
# https://avantilipids.com/contact-us
# https://www.associatedmetalcast.com/contact/
# https://www.vulcan-group.com/contact-us/
#  https://sbslp.com/contact-us/
# https://www.polsonlawfirm.com/contact-us.html
# https://www.tstech.com/contact.php
# https://www.ghafari.com/about/contact
# https://www.dynamicmanufacturinginc.com/contact-us/
# https://www.gwsys.net/contact/
# https://www.palletchief.com/contact-us
# https://www.challenge-mfg.com/contact-us/


form = AutomateForm(PATH, url)

form.waitForTitle()

firstname = 'sam'
lastname = 'wisdom'
phone = "+234080000000"
email = "sam@gmail.com"
message = "message, text, quest comment"
form.select_value_in_selectBox()


form.find_and_set_field('name', f"{lastname} {firstname}", '_email')

form.find_and_set_field('first', f"{firstname}", '_email')

form.find_and_set_field('last', f"{lastname}", '_email')

form.find_and_set_field('phone', phone, '_phone')

form.find_email_and_set_field(email, '_email')

form.find_messaage_box_and_set_field(message, '_message')

# form.solve_robot_captcha()


time.sleep(100)

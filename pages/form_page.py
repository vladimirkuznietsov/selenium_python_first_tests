import time

from selenium.webdriver import Keys
from selenium.webdriver.support.color import Color

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):
    options_names = ['Text Box',
                     'Check Box',
                     'Radio Button',
                     'Web Tables',
                     'Buttons',
                     'Links',
                     'Broken Links - Images',
                     'Upload and Download',
                     'Dynamic Properties']

    links_names = ['Elements',
                   'Forms',
                   'Alerts, Frame & Windows',
                   'Widgets',
                   'Interactions',
                   'Book Store Application']

    def fill_first_name_field(self):
        info = next(generated_person())
        name = info.full_name.split(' ')[0]
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(name)
        return name

    def fill_last_name_field(self):
        info = next(generated_person())
        name = info.full_name.split(' ')[2]
        self.element_is_visible(Locators.LAST_NAME).send_keys(name)
        return name

    def fill_email_field(self):
        info = next(generated_person())
        email = info.email
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        return email

    def select_gender(self):
        self.element_is_visible(Locators.GENDER).click()

    def fill_mobile_field(self):
        self.element_is_visible(Locators.MOBILE).send_keys('0960181792')

    def select_subject(self):
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.ENTER)

    def select_hobbies(self):
        self.element_is_visible(Locators.HOBBIES).click()

    def attach_file(self):
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r'C:\QA courses\Python\FirstTests\text.txt')

    def fill_current_address_field(self):
        info = next(generated_person())
        address = info.current_address
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(address)
        return address

    def click_submit_button(self):
        self.element_is_visible(Locators.SUBMIT).click()

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]
        return result_text

    def get_links_names(self):
        links_list = self.elements_are_visible(Locators.NAVIGATION_LINKS)
        links_text = [i.text for i in links_list]
        return links_text

    def click_elements_link_and_get_options_names(self):
        self.element_is_visible(Locators.ELEMENTS_LINK).click()
        options_list = self.elements_are_visible(Locators.ELEMENTS_LINK_OPTIONS)
        options_text = [i.text for i in options_list]
        return options_text

    def get_mandatory_fields_colors(self):
        first_name_color = Color.from_string(
            self.element_is_visible(Locators.FIRST_NAME).value_of_css_property('border-color')).hex
        last_name_color = Color.from_string(
            self.element_is_visible(Locators.LAST_NAME).value_of_css_property('border-color')).hex
        mobile_color = Color.from_string(
            self.element_is_visible(Locators.MOBILE).value_of_css_property('border-color')).hex
        return first_name_color, last_name_color, mobile_color

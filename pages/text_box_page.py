from generator.generator import generated_person
from pages.base_page import BasePage
from locators.text_box_page_locators import TextBoxPageLocators as Locators


class TextBoxPage(BasePage):

    def get_results(self):
        results = [self.element_is_visible(Locators.CREATED_NAME),
                   self.element_is_visible(Locators.CREATED_EMAIL),
                   self.element_is_visible(Locators.CREATED_CUR_ADDRESS),
                   self.element_is_visible(Locators.CREATED_PER_ADDRESS)]
        texts = [i.text.split(':')[1] for i in results]
        return texts

    def fill_full_name_fild(self):
        info = next(generated_person())
        name = info.full_name
        self.remove_footer()
        self.element_is_visible(Locators.FULL_NAME_FIELD).send_keys(name)
        return name

    def fill_email_field(self):
        info = next(generated_person())
        email = info.email
        self.element_is_visible(Locators.EMAIL_FIELD).send_keys(email)
        return email

    def fill_current_address_field(self):
        info = next(generated_person())
        address = info.current_address
        self.element_is_visible(Locators.CURRENT_ADDRESS_FIELD).send_keys(address)
        return address

    def fill_permanent_address_field(self):
        info = next(generated_person())
        address = info.permanent_address
        self.element_is_visible(Locators.PERMANENT_ADDRESS_FIELD).send_keys(address)
        return address

    def click_submit_button(self):
        self.element_is_visible(Locators.SUBMIT_BUTTON).click()

import time

from pages.form_page import FormPage


class TestOptionsNames:

    def test_options_names(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        actual_names = form_page.click_elements_link_and_get_options_names()
        assert form_page.options_names == actual_names

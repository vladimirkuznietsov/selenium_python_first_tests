import time

from pages.form_page import FormPage


class TestEmptyFieldsSubmit:

    def test_empty_fields(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        form_page.click_submit_button()
        time.sleep(0.5)
        actual_colors = form_page.get_mandatory_fields_colors()
        for i in actual_colors:
            assert i == '#dc3545'

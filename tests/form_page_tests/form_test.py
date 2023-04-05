import time

from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        first_name, last_name, email = form_page.fill_first_name_field(), form_page.fill_last_name_field(), form_page.fill_email_field()
        form_page.select_gender()
        form_page.fill_mobile_field()
        form_page.select_subject()
        form_page.select_hobbies()
        form_page.attach_file()
        form_page.fill_current_address_field()
        form_page.click_submit_button()
        result = form_page.form_result()
        assert f'{first_name} {last_name}' == result[0], 'the form has not been filled'
        assert email == result[1], 'the form has not been filled'
        time.sleep(5)

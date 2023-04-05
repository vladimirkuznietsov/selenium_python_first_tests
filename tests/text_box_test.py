import time

from pages.text_box_page import TextBoxPage


class TestTextBox:

    def test_text_box(self, driver):
        text_box = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box.open()
        expected_values = [text_box.fill_full_name_fild(),
                           text_box.fill_email_field(),
                           text_box.fill_current_address_field(),
                           text_box.fill_permanent_address_field()]
        text_box.click_submit_button()
        actual_values = text_box.get_results()
        assert expected_values == actual_values


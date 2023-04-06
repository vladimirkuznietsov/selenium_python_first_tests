import time

from pages.check_box_page import CheckBoxPage


class TestExpandOneByOne:

    def test_expand_one_by_one(self, driver):
        checkbox_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        checkbox_page.open()
        expected_names = checkbox_page.expected_items_names
        actual_names = checkbox_page.click_expand_icons()
        for i in actual_names:
            assert i == expected_names[actual_names.index(i)]

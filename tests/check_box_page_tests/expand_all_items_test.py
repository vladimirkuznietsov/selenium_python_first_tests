import time

from pages.check_box_page import CheckBoxPage


class TestExpandAllItems:

    def test_expand_all_items(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.click_expand_all_icon()
        actual_items = check_box_page.get_all_items()
        expected_items = check_box_page.expected_items_names
        for i in actual_items:
            assert i.is_displayed()
            assert i.text == expected_items[actual_items.index(i)]


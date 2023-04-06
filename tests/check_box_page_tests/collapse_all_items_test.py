import time
import unittest

from selenium.common import NoSuchElementException

from pages.check_box_page import CheckBoxPage
from unittest import TestCase


class TestCollapseAllItems:

    def test_collapse_all_items(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.click_expand_all_icon()
        items_expanded = check_box_page.get_all_items()
        items_number_expanded = len(items_expanded)
        check_box_page.click_collapse_all_icon()
        items_collapsed = check_box_page.get_all_items()
        items_number_collapsed = len(items_collapsed)
        assert items_number_expanded == 17
        assert items_number_collapsed == 1
        assert items_collapsed[0].text == 'Home'

from pages.base_page import BasePage
from locators.check_box_page_locators import CheckBoxLocators as Locators


class CheckBoxPage(BasePage):
    expected_items_names = ['Home',
                            'Desktop',
                            'Notes',
                            'Commands',
                            'Documents',
                            'WorkSpace',
                            'React',
                            'Angular',
                            'Veu',
                            'Office',
                            'Public',
                            'Private',
                            'Classified',
                            'General',
                            'Downloads',
                            'Word File.doc',
                            'Excel File.doc']

    def click_expand_all_icon(self):
        self.element_is_visible(Locators.expand_all_icon).click()

    def get_all_items(self):
        return self.elements_are_visible(Locators.all_items)

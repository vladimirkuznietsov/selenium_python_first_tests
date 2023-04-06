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

    def click_collapse_all_icon(self):
        self.element_is_visible(Locators.collapse_all_icon).click()

    def get_all_items(self):
        return self.elements_are_visible(Locators.all_items)

    def click_expand_icons(self):
        all_items_texts = []
        for i in self.elements_are_visible(Locators.expand_icon):
            i.click()
            for j in self.elements_are_visible(Locators.expand_icon):
                j.click()

            for k in self.elements_are_visible(Locators.expand_icon):
                k.click()
                all_items = self.elements_are_visible(Locators.all_items)
                all_items_texts = [i.text for i in all_items]

            return all_items_texts

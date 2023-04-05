from pages.form_page import FormPage


class TestNavigationLinksText:

    def test_nav_links(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        actual_names = form_page.get_links_names()
        assert form_page.links_names == actual_names

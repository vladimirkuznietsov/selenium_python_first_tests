from selenium.webdriver.common.by import By


class CheckBoxLocators:
    expand_all_icon = (By.XPATH, '//div[@class="rct-options"]/button[1]')
    collapse_all_icon = (By.XPATH, '//div[@class="rct-options"]/button[2]')
    all_items = (By.XPATH, '//span[@class="rct-text"]')

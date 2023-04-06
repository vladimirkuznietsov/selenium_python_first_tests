from selenium.webdriver.common.by import By


class CheckBoxLocators:
    expand_all_icon = (By.XPATH, '//div[@class="rct-options"]/button[1]')
    collapse_all_icon = (By.XPATH, '//div[@class="rct-options"]/button[2]')
    all_items = (By.XPATH, '//span[@class="rct-text"]')
    expand_icon = (By.XPATH,
                   '//li[@class="rct-node rct-node-parent rct-node-collapsed"]/span/button')

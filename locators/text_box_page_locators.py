from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_NAME_FIELD = (By.CSS_SELECTOR, '#userName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#userEmail')
    CURRENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#currentAddress')
    PERMANENT_ADDRESS_FIELD = (By.CSS_SELECTOR, '#permanentAddress')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#submit')
    CREATED_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CUR_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PER_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

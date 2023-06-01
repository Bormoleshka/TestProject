from BaseApp import BasePage
from selenium.webdriver.common.by import by
import logging
import yaml

class TestSearchLocators:
    ids = dict()
        with open("./locators.yaml") as f:
            locators = yaml.safe_load(f)
        for locator in locators["xpath"].keys():
            ids[locator] = (By.XPATH, locators["xpath"][locator])
        for locator in locators["css"].keys():
            ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
            
class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
        
    def click_button(self, locator, description=None)
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True
        
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find {text} in field {element_name}" )
        return text
        
        
        
        
    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], login, description="login form")
        
    def enter_password(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], password, decription="password form")
    
    
    def enter_your_name(self, username):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], username, description="name form")
        
        
    def enter_email(self, email):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], email, description="email form")
        
        
    def enter_content(self, content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], contentpost, description="content form")
        
    def enter_title(self, title):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], title, description="title form")
        
    def enter_descriptionpost(self, descriptionpost):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"], descriptionpost, description="description form")
        
    def enter_contentpost(self, contentpost):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENTPOST_FIELD"], contentpost, description="content form")
        
        
    
        
    
        
# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description="Login")
        
    def click_contact_button(self):
       self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description="Contact")
        
    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description="Contact us")
        
    def click_new_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_NEW_POST_BTN"], description="new post")
        
    def click_save_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BTN"], description="save")
        
# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description="text")
        
    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text
        
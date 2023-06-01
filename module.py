import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

with open("D:\Учеба\Автотестирование\Семинар_2/testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]





def find_element(self, mode, path):
    if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
    elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
    else:
            element = None
    return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return (element.value_of_css_property(property))

    

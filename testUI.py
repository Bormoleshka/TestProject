from testpage import OperationsHelper
import logging
import yaml




def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Contact button testing")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    testpage.click_contact_button()
    
def test_step3(browser):
    logging.info("Enter fields testing")
    testpage = OperationsHelper(browser)
    testpage.enter_your_name(testdata["name"])
    testpage.enter_email(testdata["email"])
    testpage.enter_content(testdata["content"])
    
def test_step4(browser):
    logging.info("CONTACT US button and alert testing")
    testpage = OperationsHelper(browser)
    testpage.click_contact_us_button()
    assert testdata.get_alert_text() == "Form succesfully submitted"
    return testdata.get_alert_text(text1)
    
def test_step5(browser):
    logging.info("Click new post button")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_button()
    
def test_step6(browser):
    logging.info("create a  new post ")
    testpage = OperationsHelper(browser)
    testpage.enter_title(testdata["title"])
    testpage.enter_descriptionpost(testdata["descriptionpost"])
    testpage.enter_contentpost(testdata["contentpost"])
    testpage.click_save_button()


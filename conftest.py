import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome imrport ChromeDriverManage
import requests




with open("D:\Учеба\Автотестирование\Семинар_2/testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]
    name = testdata['login']
    passwd = testdata['password']
    title = testdata['title']
    descriptionAPI = testdata['descriptionpost']
    contentAPI = testdata['contentpost']
    username = testdata['username']
    
# API
@pytest.fixture()
def get(token):
    logging.info("Getting token ")
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X=Auth-Token': token}, params={'owner': 'notMe'})
    listcont = [i['content'] for i in g.json()['data']
    return listcont
    
@pytest.fixture()    
def auth():
    request = requests.post('https://test-stand.gb.ru/gateway/login', testdata={'username': name, 'password': passwd})
    return request.json()['token']
    
pytest.fixture()
def newpost():
    r = requests.post('https://test-stand.gb.ru/gateway/posts', testdata={'title':title,'description':descriptionAPI,'content':contentAPI})
    return r.json()['token']
    
@pytest.fixture()
def text1():
    assert 'жареные сосиски' in get(auth)
    
@pytest.fixture()
def text2():
    return 'Йоркширский терьер'

# UI
@pytest.fixture(scope="session"):
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        
    yield driver
    driver.quit()
        
        


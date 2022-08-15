import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="function", autouse="True")
def web_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()
    
def pytest_addoption(parser):
    parser.addoption("--baseurl", action='store', default='https://wwwuat3.4wheelparts.com')
    parser.addoption("--auth", action='store', default='https://uat:uattap123@wwwuat3.4wheelparts.com')
    parser.addoption("--site", action='store', default='4WP-US')
    parser.addoption("--env", action='store', default='UAT3')
    
def pytest_configure(config):
    os.environ['baseurl'] = config.getoption('baseurl')
    os.environ['auth'] = config.getoption('auth')
    os.environ['site'] = config.getoption('site')
    os.environ['env'] = config.getoption('env')

@pytest.fixture
def get_auth(request):
    basicauth = str(os.getenv('auth'))
    request.cls.basicauth = basicauth
    return basicauth

@pytest.fixture
def get_baseurl(request):
    baseurl = str(os.getenv('baseurl'))
    request.cls.baseurl = baseurl
    return baseurl

@pytest.fixture
def get_site(request):
    site = str(os.getenv('site'))
    request.cls.site = site
    return site

@pytest.fixture
def get_env(request):
    site_env = str(os.getenv('env'))
    request.cls.site_env = site_env
    return site_env

@pytest.mark.usefixtures("web_driver", "get_auth", "get_baseurl", "get_site", "get_env")
class BaseDriver:
    pass
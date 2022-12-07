import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import streamlit as st
from  Utilities.configReader import ConfigReader
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.ExcelManupulation import  ExcelManupulation
from Utilities import configReader
#To run a script : py.test .\test_signup.py -s -v --browser "firefox" --datafile "testdata.xlsx" --worksheet "LoginTest" --tcid "TS0001"

@pytest.fixture(scope="class")
def initialize(request,browser,config,datafile,worksheet,tcid):
    
    excel = ExcelManupulation("./Test Data/" + datafile)
    excel.read_worksheet(worksheet)
    data = excel.read_AllTestData(tcid)

    if request.cls is not None:

        request.cls.browser=browser
        request.cls.config_file=config
        request.cls.datafile = datafile
        request.cls.excel = excel
        request.cls.data = data
        request.cls.tcid=tcid
        request.cls.worksheet=worksheet
    yield
    try:
        pass
    except:
        pass

def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser Type")
    parser.addoption("--datafile",help="Input File Name")
    parser.addoption("--worksheet", help="Worksheet Name")
    parser.addoption("--config", help="Configuration File Name")
    parser.addoption("--tcid", help="Testcase ID")
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture(scope="session")
def config(request):
    return request.config.getoption("--config")
@pytest.fixture(scope="session")
def datafile(request):
    return request.config.getoption("--datafile")
@pytest.fixture(scope="session")
def worksheet(request):
    return request.config.getoption("--worksheet")
@pytest.fixture(scope="session")
def tcid(request):
    return request.config.getoption("--tcid")


@pytest.fixture(scope="class")
def get_browser(request):
    print("request.cls.browser",request.cls.browser)
    if request.cls.browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if request.cls.browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = driver

    basic_config = ConfigReader('./Config Files/Basic_Setup.ini')
    url_str=str(basic_config.get_data_from_a_section("basic info","url")).strip()

    implicitly_wait=int(basic_config.get_data_from_a_section("basic info","implicitly_wait"))
    url_str=url_str.replace("'", '')
    driver.get(url_str)
    driver.maximize_window()
    driver.implicitly_wait(implicitly_wait)

    yield driver
    driver.quit()
'''
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


'''
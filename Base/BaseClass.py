from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class BaseClass():
    # Class Variable

    def __init__(self):
        # Instance Variable
        pass
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

print(driver)
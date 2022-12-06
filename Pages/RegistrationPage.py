from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class RegistrationPage(BasePage):

    def __init__(self, driver,config):
        super().__init__(driver)
        self.config=config
    def fillForm(self, name, phoneNum, email, country, city, username, password):

        self.set("name_XPATH", name)

        self.set("name_XPATH",name)
        self.set("phone_XPATH",phoneNum)
        self.set("email_XPATH",email)
        self.select("country_XPATH",country)
        self.set("city_XPATH",city)
        self.set("username_XPATH",username)
        self.set("password_XPATH",password)
        #self.click("submit_XPATH")


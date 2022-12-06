import inspect
import os
import sys
import time
#py.test .\test_signup.py -s -v --browser "chrome" --datafile "Test Data.xlsx" --worksheet "Claim Submission" --tcid "TS0001" --config "configuration.ini"
import allure


import pytest
from allure_commons.types import AttachmentType
from Base.Generic import *
from Utilities.ExcelManupulation import ExcelManupulation
from Base.Generic import Generic
from selenium.webdriver.support import expected_conditions as EC
from Utilities.configuration import Configuration


@pytest.mark.usefixtures("initialize")
class Test_SignUp():

    @pytest.fixture(autouse=True)
    def test_initialize(self,initialize,get_browser):

        config_file = "./Config Files/" + self.config_file
        config_data=Configuration()
        scriptName=os.path.basename(__file__)
        scriptName=scriptName.replace(".py","")

        self.generic = Generic( config_file,config_data,self.excel,self.data, self.driver,scriptName,Test_SignUp.__name__)
        self.generic.Configuration=Configuration()



    def test_run(self):



        try:

            if self.generic.config_data.sProcessSheetName == "" :
                self.generic.config_data.sProcessSheetName = "Test Data";
            if self.generic.config_data.sTestcaseId == "":
                self.generic.config_data.sTestcaseId = "TS0002";

            if self.generic.config_data.sLoginSheetName == "":
                self.generic.config_data.sLoginSheetName = "Login";

            if self.generic.config_data.sLoginId == "":
                self.generic.config_data.sLoginId = "FMS_0001";

            if self.generic.config_data.sDateInDDMMYYY == "":
                self.generic.config_data.sDateInDDMMYYY = self.generic.func_GetDateInDDMMYYYYFormat();
            if self.generic.config_data.sNewTestCaseName == "":
                self.generic.config_data.sNewTestCaseName = "test_signup";

            self.generic.config_data.sInputFileName = "Test Data.xlsx";
            excel = ExcelManupulation(".\\Test Data\\"+self.generic.config_data.sInputFileName)

            excel.read_worksheet(self.generic.config_data.sProcessSheetName)
            self.generic.func_TestLogInitialization();
            self.generic.func_LogHeaderCreation();
            self.generic.func_ConsolidatedLogHeaderCreation();

            self.generic.func_TCObjective("Posting documents\nExpected Result: Used to post various documents in SAP system");


            for iCounter in self.generic.excel.getIDs(self.generic.config_data.sTestcaseId):

                    try:

                        self.generic.config_data.sTestcaseId = iCounter;
                        self.generic.func_PrintSetNo();

                        # TODO Insert code here
                        self.generic.func_ScreenCaptureWithFailMsg("Testing FaiLED FOR TESTCASE 1"  );
                        #self.generic.func_ScreenValidation('Welcome to the Test Site')
                        #self.generic.enter_details_with_ID_in_screen("Welcome to the Test Site",self.generic.config_data.sTestcaseId)
                        #self.generic.select("ENTER TO THE TESTING WEBSITE")
                        #self.generic.validate_Field("Name:_Duplicate","Name:")

                        #self.generic.enterText("email")
                        # self.generic.SelectText("country")
                        # time.sleep(3)
                        # self.generic.clickonField("Submit")
                        #self.generic.checkbox_Select("bmwcheck")
                        # self.generic.validate_checkbox_Checked("hondacheck")
                        # self.generic.checkbox_UnSelect("hondacheck")
                        # self.generic.validate_checkbox_Unchecked("hondacheck")
                        # self.generic.radiobutton_Select("benzradio")
                        # self.generic.validate_radiobutton_Checked("benzradio")
                        # self.generic.radiobutton_UnSelect("benzradio")
                        # self.generic.validate_radiobutton_Unchecked("benzradio")
                        # self.generic.getRowsCountInATable("product")
                        # self.generic.getHeaderCountInATable("product")
                        # self.generic.getHeaderNamesOfATable("product")
                        # self.generic.getAllDataFromTable("product")
                        # self.generic.getDataFromSpecific_Row_Col_FromTable(1,3,"product")

                        #self.generic.scrolldown(1177, 561)
                        #self.generic.switchToIFrameUsingID("iframe")

                        #time.sleep(2)

                        # Search course

                       # self.generic.clickonField("support")
                       # time.sleep(3)
                        #self.generic.enterText("support")
                        #self.generic.scrollup(1177, 561)
                        #self.generic.swithBackToParentWindowFromIFrame()

                        # self.generic.enter_details_with_ID_in_screen("Welcome to the Test Site",self.generic.config_data.sTestcaseId)
                        # self.generic.clickonField("Signin")
                        # self.generic.func_ScreenValidation("Welcome to the Test Site")
                        # self.generic.enter_details_with_ID_in_screen("Login",self.generic.config_data.sTestcaseId)
                        # self.generic.clickonField("Signup")
                        #self.generic.rightClick("popup_pic")

                        #End Of Script Development

                    except Exception as e:
                        print("error:",e)

                        self.generic.func_ScreenCaptureWithFailMsg("Testing Failed : " +str(e) );




        except Exception as e1:
            self.generic.func_ScreenCaptureWithFailMsg("Testing Failed : " + str(e1) );

        finally:

            try:

                self.generic.func_LogBodyCreation();
                self.generic.func_SetEndTime();

                pass
            except Exception as e:
                print("Error",e)
                pass

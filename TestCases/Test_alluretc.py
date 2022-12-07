
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pytest
from Base.Generic import *
from Utilities.ExcelManupulation import ExcelManupulation
from Base.Generic import Generic
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from Utilities.configuration import Configuration


@pytest.mark.usefixtures("initialize")
class Test_hrms():

    @pytest.fixture(autouse=True)
    def test_initialize(self,initialize,get_browser):
        config_file = ConfigReader("../Config Files/" + self.config_file)
        config_data=Configuration()
        scriptName=os.path.basename(__file__)
        scriptName=scriptName.replace(".py","")

        self.generic = Generic( config_file,config_data,self.excel,self.data, self.driver,scriptName,Test_hrms.__name__)
        self.generic.Configuration=Configuration()




    def test_run(self):



        try:

            if self.generic.config_data.sProcessSheetName == "" :
                self.generic.config_data.sProcessSheetName = "Claim Submission";
            if self.generic.config_data.sTestcaseId == "":
                self.generic.config_data.sTestcaseId = "TS0001";

            if self.generic.config_data.sLoginSheetName == "":
                self.generic.config_data.sLoginSheetName = "Login";

            if self.generic.config_data.sLoginId == "":
                self.generic.config_data.sLoginId = "FMS_0001";

            if self.generic.config_data.sDateInDDMMYYY == "":
                self.generic.config_data.sDateInDDMMYYY = self.generic.func_GetDateInDDMMYYYYFormat();
            if self.generic.config_data.sNewTestCaseName == "":
                self.generic.config_data.sNewTestCaseName = "test_signup";

            self.generic.config_data.sInputFileName = "Test Data.xlsx";
            excel = ExcelManupulation("..\\Test Data\\"+self.generic.config_data.sInputFileName)
            excel.read_worksheet(self.generic.config_data.sProcessSheetName)
            self.generic.func_TestLogInitialization();
            self.generic.func_LogHeaderCreation();
            self.generic.func_ConsolidatedLogHeaderCreation();

            self.generic.func_TCObjective("Posting documents\nExpected Result: Used to post various documents in SAP system");


            for iCounter in self.generic.excel.getIDs(self.generic.config_data.sTestcaseId):

                    try:

                        self.generic.config_data.sTestcaseId = iCounter;
                        self.generic.func_PrintSetNo();

                        #allure.attach("C:\\Users\\028906744\\Documents\\selenium\\Odd Logic\\Logs\\Screenshots\\selenium_1.png",name="testlogin",attachment_type=AttachmentType.PNG)

                        # TODO Insert code here

                        # End Of Script Development

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

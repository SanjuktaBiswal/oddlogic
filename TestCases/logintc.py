import pytest
import allure
from allure_commons.types import AttachmentType
from Base.Generic import *
from Utilities.ExcelManupulation import ExcelManupulation
from Base.Generic import Generic
from selenium.webdriver.support import expected_conditions as EC

from Utilities.configuration import Configuration


@pytest.mark.usefixtures("initialize")
class Test_LoginTC():
    @pytest.fixture(autouse=True)
    def test_initialize(self,initialize,get_browser):
        config_file = "../Config Files/" + self.config_file
        config_data = Configuration()
        scriptName=os.path.basename(__file__)
        scriptName=scriptName.replace(".py","")
        self.generic = Generic( config_file,config_data,self.excel,self.data, self.driver,scriptName,Test_LoginTC.__name__)
        self.generic.Configuration = Configuration()
    def test_run(self):
            try:
                if self.generic.config_data.sProcessSheetName == "" :
                    self.generic.config_data.sProcessSheetName = 'TestData'
                if self.generic.config_data.sTestcaseId == "":
                    self.generic.config_data.sTestcaseId = 'TS0001'
                if self.generic.config_data.sLoginSheetName == "":
                    self.generic.config_data.sLoginSheetName = "";
                if self.generic.config_data.sLoginId == "":
                    self.generic.config_data.sLoginId = "";
                if self.generic.config_data.sDateInDDMMYYY == "":
                    self.generic.config_data.sDateInDDMMYYY = self.generic.func_GetDateInDDMMYYYYFormat();
                if self.generic.config_data.sNewTestCaseName == "":
                    self.generic.config_data.sNewTestCaseName  = 'Test_LoginTC';
                self.generic.config_data.sInputFileName  = 'Test Data.xlsx';
                excel = ExcelManupulation("..\\Test Data\\"+self.generic.config_data.sInputFileName)
                excel.read_worksheet(self.generic.config_data.sProcessSheetName)
                self.generic.func_TestLogInitialization();
                self.generic.func_LogHeaderCreation();
                self.generic.func_ConsolidatedLogHeaderCreation();
                self.generic.func_TCObjective ('Login System');

                for iCounter in self.generic.excel.getIDs(self.generic.config_data.sTestcaseId):
                        try:
                            self.generic.config_data.sTestcaseId = iCounter;
                            self.generic.func_PrintSetNo();
                            # TODO Insert code here
                            self.generic.enter_details_with_ID_in_screen("Welcome to the Test Site",self.generic.config_data.sTestcaseId)

                            # End Of Script Development
                        except Exception as e:
                            self.generic.func_ScreenCaptureWithFailMsg("Testing Failed : " +str(e) );
            except Exception as e1:
                print("Exception:",e1)
            finally:
                try:
                    self.generic.func_LogBodyCreation();
                    self.generic.func_SetEndTime();
                except Exception as e:
                    print("Error",e)
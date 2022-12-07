import pytest
import allure
from allure_commons.types import AttachmentType
from Base.Generic import *
from Utilities.ExcelManupulation import ExcelManupulation
from Base.Generic import Generic
from selenium.webdriver.support import expected_conditions as EC
from Utilities.configuration import Configuration


@pytest.mark.usefixtures("initialize")
class Template():
    @pytest.fixture(autouse=True)
    def test_initialize(self,initialize,get_browser):
        config_file = "./Config Files/" + self.config_file
        config_data = Configuration()
        scriptName=os.path.basename(__file__)
        scriptName=scriptName.replace(".py","")
        self.generic #
        self.generic.Configuration = Configuration()
    def test_run(self):
        try:
            if self.generic.config_data.sProcessSheetName == "" :
                self.generic.config_data.sProcessSheetName = "";
            if self.generic.config_data.sTestcaseId == "":
                self.generic.config_data.sTestcaseId = "";
            if self.generic.config_data.sDateInDDMMYYY == "":
                self.generic.config_data.sDateInDDMMYYY = self.generic.func_GetDateInDDMMYYYYFormat();
            if self.generic.config_data.sNewTestCaseName == "":
                self.generic.config_data.sNewTestCaseName #;
            self.generic.config_data.sInputFileName #;
            excel = ExcelManupulation(".\\Test Data\\"+self.generic.config_data.sInputFileName)
            excel.read_worksheet(self.generic.config_data.sProcessSheetName)
            self.generic.func_TestLogInitialization();
            self.generic.func_LogHeaderCreation();
            self.generic.func_ConsolidatedLogHeaderCreation();
            self.generic.func_TCObjective #;

            for iCounter in self.generic.excel.getIDs(self.generic.config_data.sTestcaseId):
                    try:
                        self.generic.config_data.sTestcaseId = iCounter;
                        self.generic.func_PrintSetNo();
                        # TODO Insert code here

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
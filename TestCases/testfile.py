'''
*******************************************************************************************************************
Test Case Name        :""
Brief Description     :""
                       Expected Result:""
Input Data            :
Pre-requisite         :
Author                :""
Created Date          :""
Last Modification Date:""
********************************************************************************************************************
                            Revision History
********************************************************************************************************************
Rev#:                            Reviewed By:                      Date (DD-MM-YYYY):                      Comments:
*******************************************************************************************************************/
'''
import pytest
from  Pages.RegistrationPage import RegistrationPage
from Utilities.configReader import ConfigReader
from Utilities.configuration import Configuration
from Base.Generic import Generic
@pytest.mark.usefixtures("initialize")
class Template():
        @pytest.fixture(autouse=True)
        def test_initialize(self, initialize, get_browser):
            print("Pass")
            config_file = ConfigReader('../Config Files/' + self.config_file)

            self.generic = Generic(config_file, self.excel, self.data, self.driver)

        def test_run(self):

            try:
                
                if(Configuration.sProcessSheetName==None):
                
                    Configuration.sProcessSheetName = "";
                
                if(Configuration.sTestcaseId==None):
                
                    Configuration.sTestcaseId = "DE_S8_01";
                
                if(Configuration.sLoginSheetName==None ):
                
                    Configuration.sLoginSheetName = "Login";
                
                if(Configuration.sLoginId==None ):
                
                    Configuration.sLoginId = "FMS_0001";
                
                if(Configuration.sDateInDDMMYYY==None):
                
                    Configuration.sDateInDDMMYYY = Generic.func_GetDateInDDMMYYYYFormat();
                
                if(Configuration.sNewTestCaseName==None):
                
                    Configuration.sNewTestCaseName = "";
                
                
                Configuration.sInputFileName = ".xlsx";
                print("another")
                #Generic.func_TestLogInitialization();
                Generic.self.func_ConsolidatedLogHeaderCreation();
                Generic.func_LogHeaderCreation();
                Generic.func_InitialiseVariables();
                Generic.func_NoOfTCToBeRun();
                Generic.func_TCObjective("");
                Generic.func_PrintSetNo();

                for iCounter in range(Generic.iNoOfTC):
                    if(Generic.getTCName(iCounter)):
                
                        try:

                            Configuration.sTestcaseId = Generic.getTCName(iCounter);

                            # TODO Insert code here

                            # End Of Script Development

                        except Exception as e:

                            Generic.func_ScreenCaptureWithFailMsg("Testing Failed : "+e.getMessage());

                
                
                
            except Exception as e1:
                
                    Generic.func_ScreenCaptureWithFailMsg("Testing Failed : "+e1.getMessage());
                
            finally :
                
                    try:


                      #  Generic.func_LogBodyCreation();
                      #  Generic.func_SetEndTime();
                      pass
                    except:
                         pass




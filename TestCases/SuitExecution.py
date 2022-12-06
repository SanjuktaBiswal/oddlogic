import os
import pickle
from datetime import datetime
import pandas
import pandas as pd
from bs4 import BeautifulSoup
import sys
sys.path.append('..\\')
print(os.getcwd())
from Utilities.configReader import ConfigReader


class SuitExecution():
    test_result=[]

    def __init__(self):
        basic_config = ConfigReader('../Config Files/Basic_Setup.ini')
        driver_path = basic_config.get_data_from_a_section("basic info", "driver_path")

        try:
            df=pd.read_excel(os.path.join(driver_path,"Driver File_Execution_Aurelius.xlsx"),sheet_name="Execution")
            df=df[df['Execution Status']==True]

            try:
                os.remove('outfile')
            except OSError:
                pass
            for index, row in df.iterrows():
                #print(row['Testcase'], row['Input File Name'], row['Priority'])
                os.system('cmd /c '+'py.test '+row['Testcase']+'.py -s -v --browser "chrome" --datafile \"'+row['Input File Name']+'" --worksheet "Claim Submission" --tcid "TS0001" --config "configuration.ini"')
            # os.system('cmd /c '+'py.test test_signup.py -s -v --browser "chrome" --datafile "Test Data.xlsx" --worksheet "Claim Submission" --tcid "TS0001" --config "configuration.ini"')



        except Exception as e1:
            pass

    def readtemplate(self):
        with open("..\\Template\\Consolidatedlog.html", "r") as f:
            doc = BeautifulSoup(f, "html.parser")
        return doc
    def generateHtml(self,doc,filename):
         with open(filename, "w") as f:
            f.write(str(doc))

    def addTestcaseStatus(self,doc, tcDetails):
        status = doc.find('div', id="status")
        logscript=doc.find('td', id="logscript")
        logscript.string="Test Suit Status"
        br1 = doc.new_tag("p")
        br1['style'] = 'color: blue; font-size: 14pt;'
        sdate="Execution date:"+datetime.today().strftime('%d %m %Y')
        br1.string=sdate
        status.append(br1)
        br1 = doc.new_tag("p")
        br1['style'] = 'color: blue; font-size: 14pt;'
        br1.string = "-"*(len(sdate)+10)
        status.append(br1)

        for i, data in enumerate(tcDetails):
            br1 = doc.new_tag("p")
            if "fail" in data[:4].lower():
                br1['style'] = 'color: red; font-size: 14pt;'
            elif "pass" in data[:4].lower():
                br1['style'] = 'color: green; font-size: 14pt;'

            br1.string = data

            status.append(br1)
    def generateHtmlLog(self):
        doc = self.readtemplate()
        dateString = datetime.today().strftime('%d %m %Y')
        logscript = doc.find('td', id="logscript")
        tcDetails = []
        with open('outfile', 'rb') as fp:
            tcDetails = pickle.load(fp)

        tcDetails.sort()
        self.addTestcaseStatus(doc, tcDetails)
        self.generateHtml(doc, "..\\Logs\\TestSuitExecution_"+dateString+".html")


SuitExecution().generateHtmlLog()
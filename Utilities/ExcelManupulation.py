import pandas as pd
import pandas as pd
import numpy as np
from pandas import ExcelWriter
import os
class ExcelManupulation():
    def __init__(self,filePath):

        self.filePath=filePath
        self.logwriter=None
        self.lastRow=0
        self.ConsolidatedlastRow=0
    def read_worksheet(self,sheet_name):
        self.excel_df = pd.read_excel(self.filePath, sheet_name=sheet_name,index_col=None)
        self.excel_df=self.excel_df.fillna("")

        indices = []
        columns = self.excel_df.columns.tolist()
        for ind, data in enumerate(self.excel_df.iloc[0, :].values):
            if data.lower() == 'Screen name'.lower():
                indices.append(ind)

        self.dict_screen = {}
        length = len(indices) - 1

        for ind in range(length):
            rng = (indices[ind + 1]) - (indices[ind])
            self.dict_screen[columns[indices[ind]]] = [indices[ind], rng]

            if ind == length - 1:
                self.dict_screen[columns[indices[ind + 1]]] = [indices[ind + 1]]
    def read_worksheet_with_ID(self,sheet_name,ID):
        self.excel_df = pd.read_excel(self.filePath, sheet_name=sheet_name,index_col=None)
        self.excel_df=self.excel_df.fillna("")
        self.excel_df_ID=self.read_AllTestData(ID)

        indices = []
        columns = self.excel_df_ID.columns.tolist()
        for ind, data in enumerate(self.excel_df_ID.iloc[0, :].values):

            if  str(data).lower() == 'Screen name'.lower():
                indices.append(ind)

        self.dict_screen_ID = {}
        length = len(indices) - 1

        for ind in range(length):
            rng = (indices[ind + 1]) - (indices[ind])
            self.dict_screen_ID[columns[indices[ind]]] = [indices[ind], rng]

            if ind == length - 1:
                self.dict_screen_ID[columns[indices[ind + 1]]] = [indices[ind + 1]]

    def read_AllTestData(self,tcid):
        self.testdata=self.excel_df[self.excel_df['TC ID'].str.contains(tcid)]#.iloc[:,1:]
        return self.testdata
    def get_Alldata_In_Screen(self,screen):
        temp = self.dict_screen[screen]

        data=None
        if len(temp) == 2:
            data=pd.concat([self.excel_df.iloc[:,0:2 ],self.excel_df.iloc[:, temp[0] + 1:temp[0] + temp[1]]],axis=1)

        elif len(temp) == 1:
            data=pd.concat([self.excel_df.iloc[:,0:2 ],self.excel_df.iloc[:, temp[0] + 1:]],axis=1)
        data = data.loc[(data != "").any(axis=1)]

        return data

    def get_Alldata_With_TCID_In_Screen(self,screen,TCID):

        temp = self.dict_screen[screen]
        data = None
        if len(temp) == 2:
            data = pd.concat([self.excel_df.iloc[:, 0:2], self.excel_df.iloc[:, temp[0] + 1:temp[0] + temp[1]]], axis=1)

        elif len(temp) == 1:
            data = pd.concat([self.excel_df.iloc[:, 0:2], self.excel_df.iloc[:, temp[0] + 1:]], axis=1)
        data = data.loc[(data != "").any(axis=1)]
        data=data[data["TC ID"]==TCID]

        return data
    def testdata_To_List(self,tcid):
        self.read_AllTestData( tcid)
        self.testdata_li=self.testdata.values.tolist()
        return self.testdata_li
    def set_TestCase_ID(self,TC_ID):
        self.TC_ID=TC_ID
    def update_Cell(self,colname,data):
        index = self.testdata[self.testdata['TC ID'] == self.TC_ID.strip()].index
        self.excel_df.at[index, colname] = data
    def get_Data_Column(self,colName):
       return list(self.testdata.apply(self.getData,colname="Family ID",axis=1))
    def filesave(self):
        self.writer.save()
    def set_Column_Width__BasedOn_Name(self,worksheet,width,columnName='A',format=None):
        worksheet.set_column(columnName.upper()+':'+columnName.upper(), int(width),format)
    def set_Column_Width_BasedOn_Number(self,worksheet,width,columnNumber=0,format=None):
        self.workbook.worksheet.set_column(int(columnNumber),int(columnNumber), int(width),format)
    def write_data_to_cell(self,row,col,data,format=None):
        self.workbook.worksheet.write(int(row), int(col),data,format)
    def create_new_worksheet(self,sheet):
        self.worksheet = self.workbook.add_worksheet(sheet)
    def refer_existing_worksheet(self,sheet_name):        
        self.worksheet = self.writer.sheets[sheet_name]
    def write_To_Excel(self,fileName,sheet_name,startrow=0,startcol=0):
        self.writer = pd.ExcelWriter(fileName, engine='xlsxwriter')
        self.excel_df.to_excel(self.writer, sheet_name=sheet_name, startrow=0, startcol=0, header=True, index=False)

        columns=self.excel_df.columns.tolist()
        values=self.excel_df.values.tolist()
        self.workbook = self.writer.book
        self.worksheet = self.writer.sheets['Claim Submission']
        self.border_format = self.workbook.add_format({'border': 1, 'valign': 'top'})
        self.header = self.workbook.add_format({'border': 1,'bold': True, 'valign': 'top'})
        self.header.set_align('vcenter')
        self.header.set_bg_color('#FF7F3F')


        self.screen = self.workbook.add_format({'border': 1, 'bold': True, 'valign': 'middle'})
        self.screen.set_align('vcenter')
        self.screen.set_bg_color('#7FB77E')


        self.header2 = self.workbook.add_format({'border': 1,'bold': True})

        self.header2.set_align('vcenter')
        self.header2.set_bg_color('#FBDF07')

        for ind,col in enumerate(columns):
            self.worksheet.write(0, ind, col, self.header)
            self.worksheet.set_column(0, ind, 25)

        for ind,data in enumerate(values[0:]):
            for ind2,data2 in enumerate(data):
                    if ind==0:
                        if data2.strip()=='':
                            self.worksheet.write(ind + 1, ind2, data2, self.header2)

                        else:
                            self.worksheet.write(ind + 1, ind2, data2, self.screen)
                            self.worksheet.write(ind, ind2, columns[ind2], self.screen)
                    else:
                        self.worksheet.write(ind+1, ind2, data2, self.border_format)
        #self.worksheet.conditional_format('A:Z', {'type': 'no_blanks', 'format': self.border_format})
        self.writer.save()
    def getData(self,x, colname):
        return x[colname]
    def getIDs(self, ID):

        return self.excel_df[(self.excel_df["TC ID"].str.contains(ID, case=False)) & (self.excel_df["Multiple Run Required"].str.contains("yes", case=False))]["TC ID"].tolist()


#excel=ExcelManupulation("Test Data/Test Data.xlsx")

#excel.read_worksheet("Claim Submission")

#data=excel.read_AllTestData("TS0001")
#excel.read_worksheet_with_ID("Claim Submission","TS0001")
#print(excel.get_Alldata_In_Screen("Active Plan By Plan Code"))
#print(excel.get_Alldata_With_TCID_In_Screen("Active Plan By Plan Code","TS0001_02"))
#print(excel.getIDs("TS0001"))


#print("==============================")







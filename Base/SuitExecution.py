import configparser
import tkinter as tk
from tkinter import filedialog, simpledialog
import os
from tkinter import messagebox
import pandas as pd
import sys
import inspect
import pytest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from Utilities.configReader import ConfigReader
root = tk.Tk()
root.withdraw()
#USER_INP = simpledialog.askstring(title="Enter Driver File Path",prompt='C:/Users/028906744/Desktop/Test Suit/Driver File_Execution.xlsx')
USER_INP='C:/Users/028906744/Desktop/Test Suit/Driver File_Execution.xlsx'
df= pd.read_excel(USER_INP, sheet_name='Execution')
config= pd.read_excel(USER_INP, sheet_name='Config')
df=df.fillna('')
config=config.fillna('')

browsers=config.loc[0, 'Browser For Testing']
browsers=browsers.split(",")
browser=''
def process(x):
    global browser

    if(x['Execution Status']):

        pytest.main(
            [os.path.join(config.loc[0, 'Project Path'], "TestCases", "test_signup.py"), "-s", "-v", "--browser",
             browser, "--datafile",x['Input File Name'] ,
             "--worksheet", x['Worksheet'], "--tcid",x['TC ID'], "--config",
            x['Configuration']])

for browser in browsers:

    df.apply(process,axis=1);
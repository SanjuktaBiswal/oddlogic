import configparser
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox


import pandas as pd

root = tk.Tk()
root.withdraw()
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from Utilities.configReader import ConfigReader
messagebox.showinfo("Configuration File", "Select The .ini File to compare")

basic_config = ConfigReader(os.getcwd()+"\\..\\"+"Config Files\\Basic_setup.ini")
projectPath=os.getcwd()+"\\..\\"+"Config Files\\"+basic_config.get_data_from_a_section("basic info", "default_config_file")
basic_config = ConfigReader(projectPath)

unique_screens=set()
for data in basic_config.get_all_sections():
    unique_screens.add(data.split("_")[0])
dict_screens={}

file_path = filedialog.askopenfilename()
#print(file_path)

compare_config = ConfigReader(file_path)
config = configparser.ConfigParser()
for data in compare_config.get_all_sections():
    temp_screen=data.split("_")[0]

    if temp_screen in unique_screens:
        dict_screens[data.split("_")[0]]=temp_screen+"-Duplicate"
        temp_screen=temp_screen+"_"+"_".join(data.split("_")[1:])+"_Duplicate"
        try:
            config.add_section(temp_screen)
        except:
            pass
    for data2 in compare_config.get_all_options_in_a_section(data):
        try:
            config.set(temp_screen, str(data2), str(compare_config.get_data_from_a_section(data,data2)))
        except:
            config.set(temp_screen, str(data2), data)
with open(file_path, 'w') as configfile:
    config.write(configfile)


messagebox.showinfo("CSV File", "Select The CSV to compare")
csv_path = filedialog.askopenfilename()
df=pd.read_csv(csv_path)
df.rename(columns = dict_screens, inplace = True)
for data in df.columns.tolist():
    if "Unnamed:" in data:
        df.drop(data,axis=1,inplace=True)

df.to_csv(csv_path,index=False)


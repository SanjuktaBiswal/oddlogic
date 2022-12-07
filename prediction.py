import pandas as pd
import datetime as dt
import os
import connect
import copy
import streamlit as st
import numpy as np
import time
import statsmodels.api as sm
import streamlit.components.v1 as components
import base64
import glob
import requests
from bs4 import BeautifulSoup
from AccessValidation import Access
import predict_base_model
import os
from os.path import exists
import random
import  pickle
df_upload=None
config=None

browser=''
def process(x):
    global browser
    import pytest
    if(x['Execution Status']):
        st.session_state['status_predict_placeholder'].warning("Executing Testcase "+x['Testcase'])
        
      
        pytest.main(
            [os.path.join(config.loc[0, 'Project Path'], "TestCases", x['Testcase']+".py"), "-s", "-v", "--browser",
             browser, "--datafile",x['Input File Name'] ,
             "--worksheet", x['Worksheet'], "--tcid",x['TC ID'], "--config",
            x['Configuration']])
       
def app():
    global config,df_upload,browser
    st.session_state['customer']=None
    st.session_state['option']=None
    placeholder=st.empty()   
    st.session_state['chkbox_csv_file']=False 
    if True or st.session_state['userid']!="":
        st.success("Logged in as "+st.session_state.userid)
        st.session_state['user_data']=None
        st.write("""
        # Prediction
        """)
        st.write(":heavy_minus_sign:" * 47) 
        
        background_color='#F5F5F5'
       
        
        model_names =[];
        
        temp=r'config\customers.txt'
        with open(temp) as f:
            contents = f.readlines()
            
            for line in contents:
                
                if '\n'  in line :
                    model_names.append(line[:line.index("\n")])
                else:
                    model_names.append(line)
        
            
        with st.form(key="magic"):
            
            #st.write(os.getcwd())
            if 'counter_magic' not in st.session_state:
                st.session_state['counter_magic']=0
            else:
                st.session_state['counter_magic']=0
            
            col1,col2,col3,col4=st.columns([1.5,0.2,1.5,0.5])
            with col1:
               
                Analyse_CSV = st.empty()
                csv=Analyse_CSV.checkbox('Use CSV/Excel File For Prediction')
                uploaded_file = st.file_uploader("Upload your Data File in CSV/XLS/XLSX Format",type=['csv','xlsx','xls'])#type=['png','jpeg']
                
                if uploaded_file is not None:
                 
                  df_upload= pd.read_excel(uploaded_file, sheet_name='Execution')
                  config= pd.read_excel(uploaded_file, sheet_name='Config')
                  
                  
                 
            with col2:
                pass
            with col3:
                
              st.write('')
              st.write('')
              st.write('')
              st.write('')
              st.write('')
              flag=st.form_submit_button('Predict')
                        
                
           
            with col4:
                
                pass
            if flag:
               if csv:
                 st.session_state['chkbox_csv_file']=True
                 st.session_state['status_predict_placeholder'].warning("Processing Data")
                 df_upload=df_upload.fillna('')
                 config=config.fillna('')
                 browsers=config.loc[0, 'Browser For Testing']
                 browsers=browsers.split(",")
                 browser=''
                 dataTodisplay=None
                 if os.path.exists('outfile'):
                     os.remove('outfile')
                     
                     
                 for browser in browsers:
                     df_upload.apply(process,axis=1);
                     
                 try:
                     itemlist = []
                     
                     
                         
                     if os.path.isfile('outfile'):
                         with open('outfile', 'rb') as fp:
                             itemlist = pickle.load(fp)
                     tempdict={}
                     for data in itemlist:
                         temp=data.split(":")
                         if 'Testcase' in tempdict:
                             templist=tempdict['Testcase']
                             templist.append(temp[1].strip())
                             tempdict['Testcase']=   templist
                             
                             templist2=tempdict['Status']
                             templist2.append(temp[0].strip())
                             tempdict['Status']=   templist2
                         else:
                             tempdict["Testcase"]=[temp[1].strip()]
                             tempdict["Status"]=[temp[0].strip()]
                     
                     dataTodisplay=pd.DataFrame(tempdict)
                     

                 except Exception as e:
                     print("Error:", e)
                 st.session_state['status_predict_placeholder'].warning("Processing Complete")
                 st.session_state['predict_result'].write(dataTodisplay)
               #predict_base_model.app()
               else:
               
                  df_upload= pd.read_excel( st.session_state['data_external'], sheet_name='Execution')
                  config= pd.read_excel( st.session_state['data_external'], sheet_name='Config')
                  st.session_state['status_predict_placeholder'].warning("Processing Data")
                  df_upload=df_upload.fillna('')
                  config=config.fillna('')
                  browsers=config.loc[0, 'Browser For Testing']
                  browsers=browsers.split(",")
                  browser=''
                  
                  for browser in browsers:
                  
                      df_upload.apply(process,axis=1);
                  st.session_state['status_predict_placeholder'].warning("Processing Complete")
              
                
               
                            
        if 'status_predict_placeholder' not in st.session_state:
                 st.session_state['status_predict_placeholder']=st.empty()                
                            
                           
        if 'predict_result' not in st.session_state:
             st.session_state['predict_result']=st.empty() 
        if 'predict_header' not in st.session_state:
             st.session_state['predict_header']=st.empty() 
        if 'predict_df' not in st.session_state:
             st.session_state['predict_df']=st.empty()                   
    else:
        placeholder.warning("Kindly Login To Access The Page")
       

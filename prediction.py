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
def app():
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
                print("--------")
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
                  user_data =None
                  try:
                      user_data=pd.read_csv(uploaded_file)
                  except:
                      user_data=pd.read_excel(uploaded_file)
                  
                  st.session_state['user_data']=user_data
            with col2:
                pass
            with col3:
                st.session_state['data_external'] = st.text_input('GIT url To download csv File.(Click on View raw and Copy the URL)')
                if len(model_names)>0:
                    option = st.selectbox(
                   'Select the Desired Model',
                        model_names)
                else:
                    st.subheader("No Model is Avaliable to Select")
                
           
            with col4:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                flag=st.form_submit_button('Predict')
       
            if flag:
               if csv:
                 st.session_state['chkbox_csv_file']=True
               st.session_state['status_predict_placeholder'].warning("Processing Data")
                   
               predict_base_model.app()
                
               
                            
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
       

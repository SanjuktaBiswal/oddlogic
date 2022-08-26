import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import base64
from sklearn.ensemble import RandomForestClassifier
import streamlit.components.v1 as components
import plotly.graph_objects as go
from  multipage import MultiPage
import login,signup,settings,training#,Home,report,Home_SeatAllocation,resource_report
from PIL import  Image

try:
    st.set_page_config(layout="wide")
except:
    pass

header=st.container()

timestr=time.strftime('%Y%m%d%H%M%S')
features=st.container()
df_result=None

background_color='#F5F5F5'
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
def text_downloader(raw_text,file,filename):
    csvfile=file.to_csv(index = False)
    b64=base64.b64encode(csvfile.encode()).decode()
    new_filename=filename+"_{}.csv".format(timestr)
    href=f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Download File</a>'
    st.markdown(href,unsafe_allow_html=True)

"""Simple Login App"""
# Create an instance of the app 


if 'msg' not in st.session_state:
        st.session_state['msg']=None
if 'placeholder_msg' not in st.session_state:
        st.session_state['placeholder_msg']=None
if 'userid' not in st.session_state:
        st.session_state['userid']=""
if 'pw' not in st.session_state:
        st.session_state['pw']=""
if 'app' not in st.session_state:
        st.session_state['app']=""
if 'app_analysis' not in st.session_state:
        st.session_state['app_analysis']=""
    
#...........login Page
if 'clientaccount_access' not in st.session_state:
    st.session_state['clientaccount_access']=[]



#generate trading session


st.session_state['app'] = MultiPage()    
# Title of the main page

st.session_state['app'].add_page("Login", login.app)
st.session_state['app'].add_page("Signup", signup.app)
st.session_state['app'].add_page("Training", training.app)
#st.session_state['app'].add_page("Reports", report.app)
#st.session_state['app'].add_page("Resource Reports", resource_report.app)
st.session_state['app'].add_page("Settings", settings.app)
st.session_state['app'].run()

st.write("""
# Mili's Prediction App

This app predicts the **Palmer Penguin** species!

Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)
master_usecase_output = pd.DataFrame()
placeholder = None
add_selectbox = st.sidebar.selectbox(
    'Search Options',
    ('Semantic Search', 'String Search')
)
if add_selectbox == "Semantic Search":

    with st.form(key="Semantic_Similarity"):
        # create radio button
        col1, col2, col3, col4 = st.columns([2, 3.5, 0.5, 1])
        radiobutton = col1.radio(" Select table: ", ("Search in Master usecase table", "Search in Bot description table"))

        # create an input search bar
        searchbar = col2.text_input(" Enter search string: ")

        with col4:
            st.write("")
            st.write("")
            # Create a search button
            searchbutton = st.form_submit_button(label="Search")

        st.session_state.radio = radiobutton
        st.session_state.counter_two = pd.DataFrame()
        placeholder = st.empty()

        if st.session_state.radio == "Search in Master usecase table":
            if searchbar == '':
                if searchbutton:
                    st.error("Please enter the query")

            elif (len(searchbar)>0):
                msg = placeholder.info('Fetching data. Kindly Wait...')
                left, right, right_most = st. columns([3.5, 2.5, 0.5])
                msg.subheader('Search Results')
               
                right_most.write("")
                right_most.write("")
                submitbutton = right_most.form_submit_button(label='Submit')

               

        elif st.session_state.radio == "Search in Bot description table":
            if searchbar == '':
                if searchbutton:
                    st.error("Please enter the query")

            

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'], axis=1)
df = pd.concat([input_df,penguins],axis=0)

# Encoding of ordinal features
# https://www.kaggle.com/pratik1120/penguin-dataset-eda-classification-and-clustering.
encode = ['sex','island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)

# Reads in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)


st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)

import streamlit as st
import xlsxwriter
from io import BytesIO
from userValidation import SigninDetails
import pandas as pd
import os
import numpy as np
import requests as rq
import pandas as pd
from io import BytesIO
import io,csv
url = "https://media.githubusercontent.com/media/SanjuktaBiswal/oddlogic/master/input/base_V11_Test.csv"
data = rq.get(url).content
df = pd.read_csv(url)


#download from github by providing the user id and pw
github_session = rq.Session()
github_session.auth = ("biswalsan@gmail.com", "Millan!123")
download = rq.get(url).content
#Click view raw and then copy the url
download = github_session.get("https://media.githubusercontent.com/media/SanjuktaBiswal/oddlogic/master/input/base_V11_Test.csv").content
df = pd.read_csv(io.StringIO(download.decode('utf-8')))

Collection_Credentials="Input"
oddlogic_Prediction=SigninDetails("mongodb+srv://oddlogic:oddlogic@cluster0.8qa4jjw.mongodb.net/?retryWrites=true&w=majority","oddlogic")

oddlogic_Prediction.create_Collection(Collection_Credentials) 


oddlogic_Prediction_glove=SigninDetails('mongodb+srv://oddlogic:oddlogic@cluster0.h52iyb6.mongodb.net/?retryWrites=true&w=majority',"oddlogic")

#oddlogic_Prediction_glove.create_Collection("glove") 

output=oddlogic_Prediction_glove.download_gloveFile('glove_150')
print(len(output))
embeddings_index={}
for line in output.decode('UTF-8') .splitlines():
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray(values[1:], dtype='float32')
    except:
        print (line)
    embeddings_index[word] = coefs
print(len(embeddings_index))
    
    
    
tktdata = pd.read_excel(r'Input\hon.xlsx',sheet_name='Sheet1')
#tktdata=tktdata.head(1000)


tktdata = tktdata [['Number','Short description','Assignment group','Issue Tag']]

traincolumn="Short description"
predictedcolumn="Assignment group"
# Drop the rows with empty cells in summary column
tktdata.dropna(subset=[traincolumn], inplace=True)
tktdata.dropna(subset=[predictedcolumn], inplace=True)  
unique_labs = np.unique(tktdata[predictedcolumn])
labels_index={}  # dictionary mapping label name to numeric id

for lab in unique_labs:
    label_id = len(labels_index)
    labels_index[lab] = label_id

tktdata['Codes'] = list(map(lambda x: labels_index[x], tktdata[predictedcolumn]))




tktdata_converted=pd.DataFrame.to_dict(tktdata,orient='records')
print(len(tktdata_converted))

oddlogic_Prediction.clear_inputdata()
oddlogic_Prediction.upload_inputdata(tktdata_converted)
data_from_db = oddlogic_Prediction.collection_dict["Input"].find({},{'_id':0})
data_df=pd.DataFrame.from_dict(data_from_db)
print(data_df.columns)
print(data_df.shape)

print(os.getcwd())
glovevectorfile="glove/glove_150.txt"
glove_converted = {}
with open(glovevectorfile,encoding="utf8") as f:    ##Change filename sanjukta
    for line in f:
        values = line.split()
        word = values[0]
        try:
            #coefs = np.asarray(values[1:], dtype='float32')
            coefs = values[1:]
        except:
            print (line)
        glove_converted[word] = coefs
    
print("glove:",len(glove_converted))

name="glove_150.txt"
file_location=glovevectorfile
file_data=open(file_location,'rb')
data=file_data.read()
#oddlogic_Prediction.upload_gloveFile(data,'glove_150')
output=oddlogic_Prediction.download_gloveFile('glove_150')
embeddings_index={}
for line in output.decode('UTF-8') .splitlines():
    values = line.split()
    word = values[0]
    try:
        coefs = np.asarray(values[1:], dtype='float32')
    except:
        print (line)
    embeddings_index[word] = coefs



# output=open("glove/downloadeddata.txt",'wb')
# output.write(outputdata)
# output.close()
# output = BytesIO()

# # Write files to in-memory strings using BytesIO
# # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
# workbook = xlsxwriter.Workbook(output, {'in_memory': True})
# worksheet = workbook.add_worksheet()

# worksheet.write('A1', 'Hello')
# workbook.close()

# st.download_button(
#     label="Download Excel workbook",
#     data=output.getvalue(),
#     file_name="workbook.xlsx",
#     mime="application/vnd.ms-excel"
# )
# import streamlit as st

# # Text files

# text_contents = '''
# Foo, Bar
# 123, 456
# 789, 000
# '''

# # Different ways to use the API

# st.download_button('Download CSV', text_contents, 'text/csv')
# st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

# with open('Template\\template.csv') as f:
#    st.download_button('Download CSV', f)  # Defaults to 'text/plain'

# # ---
# # Binary files

# binary_contents = b'whatever'

# # Different ways to use the API

# st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'

# with open('Template\\template.zip', 'rb') as f:
#    st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'

# # You can also grab the return value of the button,
# # just like with any other button.

# #if st.download_button(...):
# #   st.write('Thanks for downloading!')
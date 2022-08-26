# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 07:45:28 2022

@author: biswa
"""
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing
import keras
import os
from keras.layers import Input,Lambda,Dense,LSTM
from keras.models import Model
import keras.backend as k
import tensorflow as tf
print(os.getcwd())
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
sentense_encoder_layer=hub.KerasLayer(embed, input_shape=[],dtype=tf.string,trainable=False,name="USE")
model_1=tf.keras.Sequential([sentense_encoder_layer,layers.Dense(1,activation="sigmoid")],name="model_1_USE")

data=pd.read_csv(r"spam.csv",encoding='latin-1')
y=list(data['v1'])
x=list(data['v2'])
#tf.compat.v1.disable_eager_execution()
#tf.compat.v1.enable_eager_execution()
le=preprocessing.LabelEncoder()
le.fit(y)
def encoded(le,labels):
    enc=le.transform(labels)
    return keras.utils.to_categorical(enc)
def decode(le,one_hot):
    dec=np.argmax(one_hot,axis=1)
    return le.inverse_transform(dec)
test=encoded(le,['ham','ham'])
print(test.shape)
test=decode(le,test)
x_enc=x
y_enc=encoded(le,y)
x_train=np.asarray(x_enc[:5000])
y_train=np.asarray(y_enc[:5000])
x_test=np.asarray(x_enc[5000:])
y_test=np.asarray(y_enc[5000:])

def UniversalEmbedding(x):
    return embed(tf.squeeze(tf.cast(x, tf.string), axis=[1]))

input_text=Input(shape=(1,),dtype=tf.string)
embeding=Lambda(UniversalEmbedding,output_shape=(512,))(input_text)
#dense=Dense(256,activation='relu')(embeding)
print(type(embeding))
embeding=tf.concat(embeding, 1)
dense = LSTM(256,dropout=0.5,recurrent_dropout=0.5)(embeding)
#x2 = LSTM(256,dropout=0.5,recurrent_dropout=0.5)(x1)
pred=Dense(2,activation='softmax')(dense)
model=Model(inputs=[input_text],outputs=pred)
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        
with tf.compat.v1.Session()  as session:
    k.set_session(session)
    session.run(tf.compat.v1.global_variables_initializer())
    session.run(tf.compat.v1.tables_initializer())
    history=model.fit(x_train,y_train,epochs=3,batch_size=32)
    model.save_weights(r"model.h5")
    
with tf.compat.v1.Session()  as session:
    k.set_session(session)
    session.run(tf.compat.v1.global_variables_initializer())
    session.run(tf.compat.v1.tables_initializer())
    model.load_weights(r"model.h5")
    predicts=model.predict(x_test,batch_size=32)
print(predicts.shape)   
y_test=decode(le,y_test.reshape(y_test.shape[0],1))
y_predicts=encoded(le,predicts)
from sklearn import metrices
metrices.confusion_matrix(y_test,y_predicts)
print(metrices.classification_report(y_test,y_predicts))


# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:53:50 2022

@author: biswa
"""

import streamlit as st
import matplotlib.pyplot as plt

cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

width = st.sidebar.slider("plot width", 1, 50, 3)
height = st.sidebar.slider("plot height", 1, 50, 1)

fig, ax = plt.subplots(1,2,figsize=(width, height))
ax[0].plot(activity, dog, label="dog")
ax[1].plot(activity, cat, label="cat")
ax[0].legend()

st.pyplot(fig)
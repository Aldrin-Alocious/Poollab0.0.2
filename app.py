import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image('logo.png')
st.title("PoolLab")
df=st.file_uploader('Upload a CSV')
AN=df[['Unnamed: 3']]
CT=df[['Unnamed: 4']]
AN=AN.to_numpy()
CT=CT.to_numpy()
nAI=0;nCS=0;nEC=0;nME=0;nMP=0;nMA=0;nBT=0;nCL=0;
AIE=[];CSE=[];ECE=[];MEE=[];MPE=[];MAE=[];BTE=[];CLE=[];
for i in range(1,np.size(AN)):
  if CT[i,0]=='Artificial Intelligence And Machine Learning':
    nAI=nAI+1
    AIE.append(AN[i,0])
  elif CT[i,0]=='Computer Science':
    nCS=nCS+1
    CSE.append(AN[i,0])
  elif CT[i,0]=='Electronics and Communication':
    nEC=nEC+1
    ECE.append(AN[i,0])
  elif CT[i,0]=='Mechanical':
    nME=nME+1
    MEE.append(AN[i,0])
  elif CT[i,0]=='Mechanical Production':
    nMP=nMP+1
    MPE.append(AN[i,0])
  elif CT[i,0]=='Mechanical Automobile':
    nMA=nMA+1
    MAE.append(AN[i,0])
  elif CT[i,0]=='Biotechnology':
    nBT=nBT+1
    BTE.append(AN[i,0])
  elif CT[i,0]=='Civil':
    nCL=nCL+1
    CLE.append(AN[i,0])
nos=np.array([nAI,nCS,nEC,nME,nMP,nMA,nBT,nCL])
dep=np.array(['Artificial Intelligence And Machine Learning','Computer Science','Electronics and Communication','Mechanical','Mechanical Production','Mechanical Automobile','Biotechnology','Civil'])
plt.title("Admissions to Sree Chitra Thirunal College of Engineering")
plt.pie(nos,labels=dep)
st.image(plt.show())
st.write('Artificial Intelligence And Machine Learning\t- ',nAI)
st.write('Computer Science\t\t\t\t- ',nCS)
st.write('Electronics and Communication\t\t\t- ',nEC)
st.write('Mechanical\t\t\t\t\t- ',nME)
st.write('Mechanical Production\t\t\t\t- ',nMP)
st.write('Mechanical Automobile\t\t\t\t- ',nMA)
st.write('Biotechnology\t\t\t\t\t- ',nBT)
st.write('Civil\t\t\t\t\t\t- ',nCL)
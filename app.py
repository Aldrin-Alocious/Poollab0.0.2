import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image("SCT-LOGO.jpg")
st.title("POOL LAB")
df=pd.read_csv(st.file_uploader('Upload a CSV'))
st.dataframe(df)
AN=df[['Unnamed: 3']]
CT=df[['Unnamed: 4']]
AN=AN.to_numpy()
CT=CT.to_numpy()
nAI=0;nCS=0;nEC=0;nME=0;nMA=0;nBT=0;nCL=0;
AIE=[];CSE=[];ECE=[];MEE=[];MAE=[];BTE=[];CLE=[];
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
  elif CT[i,0]=='Mechanical Automobile':
    nMA=nMA+1
    MAE.append(AN[i,0])
  elif CT[i,0]=='Biotechnology':
    nBT=nBT+1
    BTE.append(AN[i,0])
  elif CT[i,0]=='Civil':
    nCL=nCL+1
    CLE.append(AN[i,0])
nos=np.array([nAI,nCS,nEC,nME,nMA,nBT,nCL])
dep=np.array(['Artificial Intelligence And Machine Learning','Computer Science','Electronics and Communication','Mechanical','Mechanical Automobile','Biotechnology','Civil'])
fig1, ax1 = plt.subplots()
ax1.pie(nos, labels=dep, autopct='%1.1f%%')
ax1.axis('equal')
st.header("Admissions this year")
st.pyplot(fig1)
st.write('Artificial Intelligence And Machine Learning\t- ',nAI)
st.write('Computer Science\t\t\t\t- ',nCS)
st.write('Electronics and Communication\t\t\t- ',nEC)
st.write('Mechanical\t\t\t\t\t- ',nME)
st.write('Mechanical Automobile\t\t\t\t- ',nMA)
st.write('Biotechnology\t\t\t\t\t- ',nBT)
st.write('Civil\t\t\t\t\t\t- ',nCL)
AIE=np.array(AIE,ndmin=2)
CSE=np.array(CSE,ndmin=2)
ECE=np.array(ECE,ndmin=2)
MEE=np.array(MEE,ndmin=2)
MAE=np.array(MAE,ndmin=2)
BTE=np.array(BTE,ndmin=2)
CLE=np.array(CLE,ndmin=2)
def departments(a,b,d):
  c=pd.DataFrame()
  c=c.append(df.loc[0], ignore_index=False, verify_integrity=False, sort=None)
  for i in range(0,np.size(b)):
    for j in range(1,np.size(a)):
      if b[0,i]==a[j,0]:
        c=c.append(df.loc[j], ignore_index=False, verify_integrity=False, sort=None)
        break
  return c
AI=departments(AN,AIE,df)
CS=departments(AN,CSE,df)
EC=departments(AN,ECE,df)
ME=departments(AN,MEE,df)
MA=departments(AN,MAE,df)
BT=departments(AN,BTE,df)
CL=departments(AN,CLE,df)
def seats(d):
  AT=d[['Unnamed: 6']]
  AT=AT.to_numpy()
  m=0;mq=0;nri=0;tfw=0;
  for i in range(1,np.size(AT)):
    if AT[i]=='Merit':
      m=m+1
    elif AT[i]=='Management Quota':
      mq=mq+1
    elif AT[i]=='NRI':
      nri=nri+1
    elif AT[i]=='TFW-Merit':
      tfw=tfw+1
  snos=np.array([m,mq,nri,tfw])
  return snos
def vacancies(d):
  AD=d[['Unnamed: 8']]
  AD=AD.to_numpy()
  AT=d[['Unnamed: 6']]
  AT=AT.to_numpy()
  vm=0;vmq=0;vnri=0;vtfw=0;
  for i in range(1,np.size(AD)):
    if AD[i]=='No':
      if AT[i]=='Merit':
       vm=vm+1
      elif AT[i]=='Management Quota':
       vmq=vmq+1
      elif AT[i]=='NRI':
       vnri=vnri
      elif AT[i]=='TFW-Merit':
       vtfw=vtfw
  vsnos=np.array([vm,vmq,vnri,vtfw])
  return vsnos
def vslashs(a,b):
  c=[];
  for i in range(0,np.size(a)):
    c.append(str(a[i])+" out of "+str(b[i]))
  return c
vdf=pd.DataFrame()
vdf['']=['Merit','Management Quota','NRI','TFW-Merit']
seat=seats(AI)
vacan=vacancies(AI)
vdf['Artificial Intelligence']=vslashs(vacan,seat)
seat=seats(CS)
vacan=vacancies(CS)
vdf['Computer Science']=vslashs(vacan,seat)
seat=seats(EC)
vacan=vacancies(EC)
vdf['Electronics and Communication']=vslashs(vacan,seat)
seat=seats(ME)
vacan=vacancies(ME)
vdf['Mechanical Engineering']=vslashs(vacan,seat)
seat=seats(MA)
vacan=vacancies(MA)
vdf['Automobile Engineering']=vslashs(vacan,seat)
seat=seats(BT)
vacan=vacancies(BT)
vdf['Biotechnology']=vslashs(vacan,seat)
seat=seats(CL)
vacan=vacancies(CL)
vdf['Civil Engineering']=vslashs(vacan,seat)
st.dataframe(vdf)
st.selectbox('Reservation Category', ['General', 'EWS', 'OEC', 'OBC', 'Latin Catholic and Anglo Indian (LA)', 'Other Backward Hindu (BH)', 'Ezhava (EZ)', 'Muslim (MU)', 'Viswakarma and related communities(VK)'])

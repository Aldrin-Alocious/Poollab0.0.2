import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image("SCT-LOGO.jpg")
st.title("POOL LAB")
df=pd.read_csv(st.file_uploader('Upload a CSV'))
st.dataframe(df)
dfz=df
g=dfz[['Unnamed: 8']]
g=g.to_numpy()
g=np.array(g,ndmin=2)
h=dfz[['Unnamed: 6']]
h=h.to_numpy()
h=np.array(h,ndmin=2)           
for i in range(1,np.size(g)):
  if g[i]=='Yes' or h[i]=='NRI' or h[i]=='TFW-Merit':
    dfz=dfz.drop([i])
k=dfz[['Unnamed: 8']]
k=k.to_numpy()
dfz=dfz.reset_index(drop=True)
dfz1=dfz
dfz2=dfz
st.dataframe(dfz)
st.write(dfz1)
st.write(dfz2)
KM=df[['Unnamed: 2']]
AN=df[['Unnamed: 3']]
CT=df[['Unnamed: 4']]
AN=AN.to_numpy()
CT=CT.to_numpy()
KM=KM.to_numpy()
def oplist(op):
  c='';
  for i in range(0,np.size(op)):
    c=str(c)+' '+str(op[i])
  return c
def decode(ss):
  z=[];
  for i in range(0,ss.count('#')):
    x=ss.partition('#')
    z.append(str(x[0]).strip())
    ss=str(x[2])
  z.append(ss.strip())
  return z
def decodeRank(ss):
  z=[];
  for i in range(0,ss.count('#')):
    x=ss.partition('#')
    z.append(int(x[0]))
    ss=str(x[2])
  z.append(int(ss))
  return z
def find1(stw,c):
  x=stw.partition('-')
  if x[0]=='AI':
    a='Artificial Intelligence And Machine Learning'
  elif x[0]=='CS':
    a='Computer Science'
  elif x[0]=='EC':
    a='Electronics and Communication'
  elif x[0]=='ME':
    a='Mechanical'
  elif x[0]=='MA':
    a='Mechanical Automobile'
  elif x[0]=='BT':
    a='Biotechnology'
  elif x[0]=='CL':
    a='Civil'
  if x[2]=='SM':
    b='Merit'
  elif x[2]=='MG':
    b='Management Quota'
  l=dfz1[['Unnamed: 4']];
  l=l.to_numpy();
  m=dfz1[['Unnamed: 6']];
  m=m.to_numpy();
  n=dfz1[['Unnamed: 7']];
  n=n.to_numpy();
  for i in range(1,np.size(l)):
    if n[i]==c or c=='jump':
      if l[i]==a and m[i]==b:
        return i
  return 0
def find2(stw,c):
  x=stw.partition('-')
  if x[0]=='AI':
    a='Artificial Intelligence And Machine Learning'
  elif x[0]=='CS':
    a='Computer Science'
  elif x[0]=='EC':
    a='Electronics and Communication'
  elif x[0]=='ME':
    a='Mechanical'
  elif x[0]=='MA':
    a='Mechanical Automobile'
  elif x[0]=='BT':
    a='Biotechnology'
  elif x[0]=='CL':
    a='Civil'
  if x[2]=='SM':
    b='Merit'
  elif x[2]=='MG':
    b='Management Quota'
  l=dfz2[['Unnamed: 4']];
  l=l.to_numpy();
  m=dfz2[['Unnamed: 6']];
  m=m.to_numpy();
  n=dfz2[['Unnamed: 7']];
  n=n.to_numpy();
  for i in range(1,np.size(l)):
    if n[i]==c or c=='jump':
      if l[i]==a and m[i]==b:
        return i
  return 0
def listop(stv):
  z=[];
  for i in range(0,stv.count(' ')):
    x=stv.partition(' ')
    z.append(x[0])
    stv=str(x[2])
  z.append(stv)
  return z
if "appno" not in st.session_state:
  st.session_state.appno=''
if "name" not in st.session_state:
  st.session_state.name=''
if "keam" not in st.session_state:
  st.session_state.keam=''
if "reserve" not in st.session_state:
  st.session_state.reserve=''
if "opti" not in st.session_state:
  st.session_state.opti=''
if "sctian" not in st.session_state:
  st.session_state.sctian=''
st.header("Form for Spot Entry")
with st.form("my_form",clear_on_submit=True):
  ga=st.text_input('Application Number')
  gb=st.text_input('Name')
  gc=st.text_input('KEAM Rank')
  gd=st.selectbox('Reservation Category', ['General', 'EWS', 'OEC', 'OBC', 'Latin Catholic and Anglo Indian (LA)', 'Other Backward Hindu (BH)', 'Ezhava (EZ)', 'Muslim (MU)', 'Viswakarma and related communities(VK)'])
  op=st.multiselect('Options', ['AI-SM','AI-MG','CS-SM','CS-MG','EC-SM','EC-MG','ME-SM','ME-MG','MA-SM','MA-MG','BT-SM','BT-MG','CL-SM','CL-MG'])
  ge=oplist(op)
  gf=st.selectbox('Already admitted?',['No','Yes'])
  submitted=st.form_submit_button(label='Submit')
  if submitted:
    st.session_state['appno']=str(st.session_state['appno'])+'#'+str(ga)
    st.session_state['name']=str(st.session_state['name'])+'#'+str(gb).upper()
    st.session_state['keam']=str(st.session_state['keam'])+'#'+str(gc)
    st.session_state['reserve']=str(st.session_state['reserve'])+'#'+str(gd)
    st.session_state['opti']=str(st.session_state['opti'])+'#'+str(ge)
    st.session_state['sctian']=str(st.session_state['sctian'])+'#'+str(gf)
    for item in st.session_state.items():
      st.write(item)
finished=st.button(label='Finish')
with st.sidebar:
  st.header("Search by name")
  if "finder" not in st.session_state:
    st.session_state.finder=''
  st.session_state['finder']=st.text_input("You can check whether a student is in the list or not").upper();
  if st.session_state['finder']==st.session_state['finder']:
    dff=df
  for i in range(1,np.size(g)):
    if not st.session_state['finder']==KM[i,0]:
      dff=dff.drop([i])
  dff.loc[len(dff.index)]=dff.loc[0]
  for i in range(0,9):
    if dff.iat[1,0]=='Sl No':
      st.write("Not found")
      break;
    else:
      st.write(dff.iat[0,i]+" : "+dff.iat[1,i])
if finished:
  a=st.session_state['appno'].lstrip('#');
  b=st.session_state['name'].lstrip('#');
  c=st.session_state['keam'].lstrip('#');
  d=st.session_state['reserve'].lstrip('#');
  e=st.session_state['opti'].lstrip('#');
  f=st.session_state['sctian'].lstrip('#');
  y1=decode(a)
  y2=decode(b)
  y3=decodeRank(c)
  y4=decode(d)
  y5=decode(e)
  y6=decode(f)
  size=len(y3)
  for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if y3[j] < y3[min_index]:
                min_index = j
        (y1[ind], y1[min_index]) = (y1[min_index], y1[ind])
        (y2[ind], y2[min_index]) = (y2[min_index], y2[ind])
        (y3[ind], y3[min_index]) = (y3[min_index], y3[ind])
        (y4[ind], y4[min_index]) = (y4[min_index], y4[ind])
        (y5[ind], y5[min_index]) = (y5[min_index], y5[ind])
        (y6[ind], y6[min_index]) = (y6[min_index], y6[ind])
  y7=[];
  for i in range(0,len(y6)):
    y7.append('')
  y8=[];
  for i in range(0,len(y6)):
    y8.append('')
  y9=[];
  for i in range(0,len(y6)):
    y9.append('')
  for i in range(0,len(y6)):
    if not y4[i]=='General':
      pp=listop(y5[i])
      pq=len(pp)
      for j in range(0,pq):
        pr=find1(pp[j],y4[i])
        if pr>0:
          if y6[i]=='Yes':
            stp=y2[i]
            NA=df[['Unnamed: 2']]
            NA=NA.to_numpy()
            for k in range(0,np.size(NA)):
              if NA[k]==stp:
                dfz1.loc[len(dfz1.index)]=df.loc[k]
                dfz1=dfz1.reset_index(drop=True)
                break;
            y7[i]=pp[j]
            dfz1=dfz1.drop([pr])
            dfz1=dfz1.reset_index(drop=True)
            continue;
          y7[i]=pp[j]
          dfz1=dfz1.drop([pr])
          dfz1=dfz1.reset_index(drop=True)
          break;
  for i in range(0,len(y6)):
    pp=listop(y5[i])
    pq=len(pp)
    for j in range(0,pq):
      pr=find2(pp[j],'jump')
      if pr>0:
        if y6[i]=='Yes':
          stp=y2[i]
          NA=df[['Unnamed: 2']]
          NA=NA.to_numpy()
          for k in range(0,np.size(NA)):
            if NA[k]==stp:
              dfz2.loc[len(dfz2.index)]=df.loc[k]
              dfz2=dfz2.reset_index(drop=True)
              break;
          y8[i]=pp[j]
          dfz2=dfz2.drop([pr])
          dfz2=dfz2.reset_index(drop=True)
          continue;
        y8[i]=pp[j]
        dfz2=dfz2.drop([pr])
        dfz2=dfz2.reset_index(drop=True)
        break;
  spotdf=pd.DataFrame()
  spotdf['Application Number']=y1
  spotdf['Name']=y2
  spotdf['KEAM Rank']=y3
  spotdf['Reservation Category']=y4
  spotdf['Opted']=y5
  spotdf['Already Admitted']=y6
  spotdf['Alloted by reservation']=y7
  spotdf['Alloted by rank']=y8
  spotdf['Alloted']=y9
  st.subheader("Spot Application List")
  sdf=spotdf.to_csv().encode('utf-8')
  spotdf=spotdf.reset_index(drop=True)
  st.dataframe(spotdf)
  st.download_button("Press to Download",sdf,"file.csv","text/csv",key='download-csv')
  st.session_state.appno=''
  st.session_state.name=''
  st.session_state.keam=''
  st.session_state.reserve=''
  st.session_state.opti=''
  st.session_state.sctian=''
  st.session_state.finder=''
  st.dataframe(dfz)
  st.dataframe(dfz1)
  st.dataframe(dfz2)
  st.balloons()
  exit()
  st.write("Failed")

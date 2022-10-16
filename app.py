import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.image("SCT-LOGO.jpg")
st.title("POOL LAB")
df=pd.read_csv(st.file_uploader('Upload a CSV'))
st.dataframe(df)
dfz=df
dfz1=df
dfz2=df
dfz3=df
g=dfz[['Unnamed: 8']]
g=g.to_numpy()
g=np.array(g,ndmin=2)
h=dfz[['Unnamed: 6']]
h=h.to_numpy()
h=np.array(h,ndmin=2)           
for i in range(1,np.size(g)):
  if g[i]=='Yes' or h[i]=='NRI' or h[i]=='TFW-Merit':
    dfz=dfz.drop([i])
    dfz1=dfz1.drop([i])
    dfz2=dfz2.drop([i])
    dfz3=dfz3.drop([i])
k=dfz[['Unnamed: 8']]
k=k.to_numpy()
dfz=dfz.reset_index(drop=True)
dfz1=dfz1.reset_index(drop=True)
dfz2=dfz2.reset_index(drop=True)
dfz3=dfz3.reset_index(drop=True)
st.dataframe(dfz)
KM=df[['Unnamed: 2']]
AN=df[['Unnamed: 3']]
CT=df[['Unnamed: 4']]
AN=AN.to_numpy()
CT=CT.to_numpy()
KM=KM.to_numpy()
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
seat1=seats(AI)
vac1=vacancies(AI)
vdf['Artificial Intelligence']=vslashs(vac1,seat1)
seat2=seats(CS)
vac2=vacancies(CS)
vdf['Computer Science']=vslashs(vac2,seat2)
seat3=seats(EC)
vac3=vacancies(EC)
vdf['Electronics and Communication']=vslashs(vac3,seat3)
seat4=seats(ME)
vac4=vacancies(ME)
vdf['Mechanical Engineering']=vslashs(vac4,seat4)
seat5=seats(MA)
vac5=vacancies(MA)
vdf['Automobile Engineering']=vslashs(vac5,seat5)
seat6=seats(BT)
vac6=vacancies(BT)
vdf['Biotechnology']=vslashs(vac6,seat6)
seat7=seats(CL)
vac7=vacancies(CL)
vdf['Civil Engineering']=vslashs(vac7,seat7)
st.header("Vacancies and Seats")
st.dataframe(vdf)
def oplist(op):
  c='';
  for i in range(0,np.size(op)):
    c=str(c)+' '+str(op[i])
  return c.strip()
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
            break;
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
          break;
        y8[i]=pp[j]
        dfz2=dfz2.drop([pr])
        dfz2=dfz2.reset_index(drop=True)
        break;
  for i in range(0,len(y6)):
    if not y7[i]=='':
      ab1=y5[i].find(y7[i])
      ab2=y5[i].find(y8[i])
      if ab1<=ab2 or y8[i]=='':
        y9[i]=y7[i]
      else:
        y9[i]=y8[i]
  for i in range(0,len(y6)):
      if not y9[i]=='':
        x=y9[i].partition('-')
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
        l=dfz3[['Unnamed: 4']];
        l=l.to_numpy();
        m=dfz3[['Unnamed: 6']];
        m=m.to_numpy();
        n=dfz3[['Unnamed: 7']];
        n=n.to_numpy();
        for j in range(1,np.size(l)):
          if n[j]==y4[i]:
            if l[j]==a and m[j]==b:
              dfz3=dfz3.drop([j])
              dfz3=dfz3.reset_index(drop=True)
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
  st.dataframe(dfz3)
  st.balloons()
  exit()
  st.write("Failed")

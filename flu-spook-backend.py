pip install -r 'https://github.com/DhasiM/Influenza_Spook/blob/main/data/requirements.txt'
import streamlit as st
import pandas as pd
import numpy as np
import warnings
import pickle
warnings.filterwarnings(action='ignore')

st.title('Flu_Spook')



from pandas import read_csv
from pandas import to_datetime
from fbprophet import Prophet

# load data

import warnings
import pandas as pd
import matplotlib.pyplot as plt
import pickle
warnings.filterwarnings(action='ignore')

DATA_URL= ('https://github.com/DhasiM/Influenza_Spook/blob/main/data/WPOFluNetInteractiveReport.csv')
data=pd.read_csv(DATA_URL, parse_dates=['EDATE'], index_col='EDATE', skiprows=3)
data.tail(1)

data = data.fillna(0) #fill any remaining gaps with 0
_=data.pop('SPEC_RECEIVED_NB') #remove the number of specimen received
_=data.pop('SPEC_PROCESSED_NB') #remove the number of specimen processed
data['SDATE'] = pd.to_datetime(data['SDATE']) #from object to datetime
data.head()

target=data.pop('TITLE')
one_hot_encoded_data = pd.get_dummies(data)
one_hot_encoded_data.tail()

cat_data=one_hot_encoded_data
df_inf=cat_data.resample('1m').mean()
df2_inf=cat_data.resample('1y').mean()
#check for seasonality, trend, 
fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)
cat_data.plot(title='All influenza', legend=False, ax=axes[0])
df_inf.plot(title='Influenza seasonality', legend=False, ax=axes[1])
df2_inf.plot(title='Influenza trend', legend=False, ax=axes[2])
#data['AH5'].pl

cat_data.head(2)

import fbprophet
# print version number
print('Prophet %s' % fbprophet.__version__)

import shutil
shutil.unpack_archive('https://github.com/DhasiM/Influenza_Spook/blob/main/data/flu_models.zip')

outbreak=pickle.load(open('../input/flu-spook-models/outbreak.sav', 'rb'))
model=pickle.load(open('../input/flu-spook-models/prophet.sav', 'rb'))

prophet_df=cat_data.reset_index()
prophet_df.rename(columns = {'EDATE':'ds', 'ALL_INF':'y'}, inplace = True)


# prepare expected column names
df= prophet_df
df['ds']= to_datetime(df['ds'])

#split data
from sklearn.model_selection import train_test_split

x_train, x_test= train_test_split(df, test_size=0.3)
x_train.sort_values(by='ds', axis=0, ascending=True, inplace=True)
x_test.sort_values(by='ds', axis=0, ascending=True, inplace=True)

prophet_df.head(2)

future_data = model.make_future_dataframe(periods=14)
#forecast the data for Test  data
forecast_data = model.predict(x_test)
model.plot(forecast_data)

from sklearn.preprocessing import LabelEncoder
# creating instance of labelencoder
labelencoder = LabelEncoder()#one hot encode the categores from label encoder
# using the encoder to encode the categorical columns
Y= labelencoder.fit_transform(target)
Y

preds = outbreak.predict(forecast_data.yhat.array.reshape(-1, 1))
y2=labelencoder.inverse_transform(preds)
y2

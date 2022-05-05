import streamlit as st
import gradio as gr
import pandas as pd
import numpy as np
import warnings
import pickle
from pandas import to_datetime
from fbprophet import Prophet
import matplotlib.pyplot as plt
#import bokeh.plotting as bk
from sklearn.preprocessing import LabelEncoder
from prophet.plot import plot_plotly, plot_components_plotly
warnings.filterwarnings(action='ignore')

st.title('Flu_Spook')

outbreak=pickle.load(open('outbreak.sav', 'rb'))
model=pickle.load(open('prophet2.sav', 'rb'))
#data=pd.read_csv('WPOFluNetInteractiveReport.csv', parse_dates=['EDATE'], index_col='EDATE', skiprows=3)


#DATA_URL = ('')
DATA_PATH='WPOFluNetInteractiveReport.csv'
@st.cache
def load_data():
    data= pd.read_csv(DATA_PATH, parse_dates=['EDATE'], index_col='EDATE', skiprows=3)
    target=data.pop('TITLE')
    return data, target

data_load_state = st.text('Loading data...')
data, target=load_data()
data_load_state.text("Done! (using st.cache)")

@st.cache
def select_year(data=data, year = None):
    if year == None:
        pass
    else:
        data=data.groupby('Year')
        data = data.get_group(year)
        return data
    
@st.cache
def select_country(data=data, country=None):
    if country == None:
        pass
    else:
        data=data.groupby('Country')
        data = data.get_group(country)
        return data
    
def process_selection(data=data):
    data = data.fillna(0) #fill any remaining gaps with 0
    _=data.pop('SPEC_RECEIVED_NB') #remove the number of specimen received
    _=data.pop('SPEC_PROCESSED_NB')
    data['SDATE'] = pd.to_datetime(data['SDATE'])
    return data, target 

data, target=load_data()
data, target=process_selection(data)


user_country=st.selectbox("Choose a country", 
                         ('Australia', 'Cambodia', 'China', 'Fiji', 'Japan',
       "Lao People's Democratic Republic", 'Malaysia', 'Mongolia',
       'New Caledonia', 'New Zealand', 'Papua New Guinea', 'Philippines',
       'Republic of Korea', 'Singapore', 'Viet Nam'))

if user_country:
    
    data=select_country(country=user_country)
    user_year=st.slider("Choose year", min_value=2000, max_value=2022, step=1)
    if user_year:
        #=select_country(country=user_country)
        data=select_year(data, year=int(user_year))
        data, target = process_selection(data)
        st.write('You have selected data for', user_country, 'for the year', user_year)
        st.dataframe(data.tail(5))





    
@st.cache   

def prophet_prediction(data=data, period=14):
    cat_data = pd.get_dummies(data)
    prophet_df=cat_data.reset_index()
    prophet_df.rename(columns = {'EDATE':'ds', 'ALL_INF':'y'}, inplace = True)
    # prepare expected column names
    data= prophet_df
    data['ds']= pd.to_datetime(data['ds'])
    data.sort_values(by='ds', axis=0, ascending=True, inplace=True)
    future_data = model.make_future_dataframe(period)
#forecast the data for Test  data
    forecast_data = model.predict(data)
    return forecast_data, future_data

forecast_data, future_data =prophet_prediction()

st.dataframe(future_data.head(5))
#def plot_forecast(forecast_data):
 #   model.plot(forecast_data)
st.subheader('Prophet forecast')
#plot=model.plot(forecast_data)
#st.plotly_chart(plot)

import plotly.express as px
from plotly.subplots import make_subplots
df= data.reset_index()
#fig = px.scatter(df, x="EDATE", y="ALL_INF")
df1= pd.concat([df, forecast_data.yhat], axis=1)
df1.rename(columns = {'yhat':'predictions'}, inplace = True)
df1.rename(columns = {'ALL_INF':'observations'}, inplace = True)
fig =px.scatter(df1, x='EDATE',y=['observations','predictions'])
#fig =px.scatter(x=df.EDATE,y=[df.ALL_INF,forecast_data.yhat])
st.plotly_chart(fig)




@st.cache
def view_trends(data=data):
    #check for seasonality, trend, 
    figs, axes = plt.subplots(1,2, figsize=(20,4), dpi=100)
    data['ALL_INF'].plot(title='All influenza', legend=False, ax=axes[0])
    df_inf=data['ALL_INF'].resample('1m').mean()
    #df2_inf=data['ALL_INF'].resample('1y').mean()
    df_inf.plot(title='Influenza seasonality', legend=False, ax=axes[1])
    #df2_inf.plot(title='Influenza trend', legend=False, ax=axes[2])
    return figs
#figs=view_trends()
#st.pyplot(figs)

@st.cache(suppress_st_warning=True)

#if st.button('view trends'):
 #   fig = view_trends()
  #  st.pyplot(fig)
    

@st.cache   
def outbreak_predictions(forecast_data=forecast_data):
    preds = outbreak.predict(forecast_data.yhat.array.reshape(-1, 1))
    labelencoder = LabelEncoder()#one hot encode the categores from label encoder
    # using the encoder to encode the categorical columns
    Y= labelencoder.fit_transform(target)
    readable_prediction=labelencoder.inverse_transform(preds)
    #y2 =
    return readable_prediction

readable_prediction= outbreak_predictions()
new_df=pd.merge(forecast_data, pd.DataFrame(readable_prediction), left_index=True, right_index=True)
#pred= pd.DataFrame(readable_prediction)
st.dataframe(new_df)
# In[14]:

flags=new_df[new_df.loc[0].str.contains("Outbreak|Pandemic")]
st.dataframe(flags)    




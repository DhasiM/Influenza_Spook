import streamlit as st
import gradio as gr
import pandas as pd
import numpy as np
import warnings
import pickle
from pandas import to_datetime
import datetime
from fbprophet import Prophet
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from prophet.plot import plot_plotly, plot_components_plotly
warnings.filterwarnings(action='ignore')

st.title('Flu_Spook')

outbreak=pickle.load(open('outbreak.sav', 'rb'))
model=pickle.load(open('prophet2.sav', 'rb'))
model1=pickle.load(open('prophet.sav', 'rb'))

DATA_PATH='WPOFluNetInteractiveReport.csv'

@st.cache #cache results of function
def load_and_process_data():
    ''' 
    This function reads the dataframe from the origin, parses it and pre-processes it.
    
    Input: DATA_PATH is the url, path or name of the file to be loaded. Here it uses .csv but
    can be modified to accept tabular data of any format.
    
    Output: Pandas dataframe loaded in memory and target column.
    '''
    data= pd.read_csv(DATA_PATH, parse_dates=['EDATE'], index_col='EDATE', skiprows=3)
    target=data.pop('TITLE')
    _=data.pop('SPEC_RECEIVED_NB') #remove the number of specimen received
    _=data.pop('SPEC_PROCESSED_NB')

    return data, target

data_load_state = st.text('Loading data...')
data, target=load_and_process_data()

data_load_state.text("Done loading!")

@st.cache #cache results of function
def select_year(data=data, year = None):
    '''
    This function allows the user to select a year of interest from the dataframe
    
    input: pre-loaded dataframe.
    
    output: reduced dataframe with only the year of interest.
    
    '''
    if year == None:
        pass
    else:
        data=data.groupby('Year')
        data = data.get_group(year)
        return data
    
@st.cache #cache results of function
def select_country(data=data, country=None):

    '''
    This function allows the user to select a country of interest from the dataframe
    
    input: pre-loaded dataframe.
    
    output: reduced dataframe with only the country of interest.
    
    '''
    if country == None:
        pass
    else:
        data=data.groupby('Country')
        data = data.get_group(country)
        return data

data, target=load_and_process_data()



#if st.sidebar.button('country'):
user_country=st.sidebar.selectbox("Choose a country", 
                         ('None','Australia', 'Cambodia', 'China', 'Fiji', 'Japan',
       "Lao People's Democratic Republic", 'Malaysia', 'Mongolia',
       'New Caledonia', 'New Zealand', 'Papua New Guinea', 'Philippines',
       'Republic of Korea', 'Singapore', 'Viet Nam'))
if user_country != 'None':
    data=select_country(country=user_country)
    start_date=min(data.Year)
    end_date= max(data.Year)
    
    st.write('You have selected data for', user_country)
            
   
    if st.sidebar.button('select year'):
        user_year = st.sidebar.slider("Choose year", min_value=2000, max_value=2022, step=1)
    
        if user_year != 'None':
        
            data=select_year(data, year=int(user_year))
            start_date=year
            end_date= year+1
            #data, target = process_selection(data)
            st.write('You have selected data for', user_country, 'for the year', user_year)
            st.dataframe(data.tail(5))
else:
    if user_country == 'None':
        start_date=min(data.Year)
        end_date= max(data.Year)
    
        if st.sidebar.button('Press Button to Filter by Year'):
            user_year = st.sidebar.slider("Choose year", min_value=2000, max_value=2022, step=1)    
            data=select_year(data, year=int(user_year))
            #data, target = process_selection(data)
            start_date=user_year
            end_date= user_year+ 1
    
            st.write('You have selected data for the year', user_year)
            st.dataframe(data.tail(5))




    
@st.cache   
def create_future(ds):
    df=ds
    for idx, model in enumerate(models):
        new=model.predict(ds)
        new[idx]= new.rename(columns={'yhat': idx}, inplace=True)
        df[idx] =new[idx]
    return df


        
@st.cache
def prophet_prediction(data=data, period=2):
    #data, target=process_selection()
    cat_data = pd.get_dummies(data)
    prophet_df=cat_data.reset_index()
    prophet_df.rename(columns = {'EDATE':'ds', 'ALL_INF':'y'}, inplace = True)
    # prepare expected column names
    data= prophet_df
    data['ds']= pd.to_datetime(data['ds'])
    data.sort_values(by='ds', axis=0, ascending=True, inplace=True)
    future_data = model1.make_future_dataframe(period)
    forecast_data = model1.predict(future_data)
    return forecast_data, future_data

forecast_data, future_data =prophet_prediction()

#st.dataframe(future_data.head(5))
#def plot_forecast(forecast_data):
 #   model.plot(forecast_data)

st.subheader('Forecast influenza data')

  
#if st.button('Choose plot limits'):
    #date = st.sidebar.slider('start date', datetime.date(2000,1,1))
    #enddate= st.sidebar.slider('end date', datetime.date(2001,1,1))
plot=model.plot(forecast_data)
ax = plot.gca()
#ax.set_xlim([start_date, end_date])

st.plotly_chart(plot)

# setting x limit. date range to plot


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




#@st.cache
#def view_trends1(data=data):
    #check for seasonality, trend, 
    #Resample at monthly and yearly intervals to observe trends and seasonality
 #   df_inf=data.resample('1m').mean()
  #  df2_inf=data.resample('1y').mean()

#check for seasonality and trend
   # fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)

#plot all the influenza subtype  and total columns
    #data.iloc[:, 3:14].plot(title='Raw Data', legend=False,  xlabel='Date', ax=axes[0]) 
   # df_inf.iloc[:, 3:14].plot(title='Influenza seasonality', legend=False,  xlabel='Date', ax=axes[1])
    #df2_inf.iloc[:, 3:14].plot(title='Influenza trend', legend=False,  xlabel='Date',  ax=axes[2])

    #figs, axes = plt.subplots(1,2, figsize=(20,4), dpi=100)
    #data['ALL_INF'].plot(title='All influenza', legend=False, ax=axes[0])
    #df_inf=data['ALL_INF'].resample('1m').mean()
    #df2_inf=data['ALL_INF'].resample('1y').mean()
    #df_inf.plot(title='Influenza seasonality', legend=False, ax=axes[1])
    #df2_inf.plot(title='Influenza trend', legend=False, ax=axes[2])
  #  return fig
#figs=view_trends()
#st.pyplot(figs)
@st.cache   
def view_trends(data=data):
    fig =px.scatter(data, x='EDATE',y=['ALL_INF', 'INF_A', 'INF_B'])
    return fig
#fig =px.scatter(x=df.EDATE,y=[df.ALL_INF,forecast_data.yhat])


#@st.cache(suppress_st_warning=True)
if st.button('view trend'):
    fig = view_trends()
    st.plotly_chart(fig)
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
reads= pd.DataFrame(readable_prediction)
#reads.rename(columns ={'0':'preds'}, inplace=True)
new_df=pd.merge(forecast_data, reads, left_index=True, right_index=True)
#pred= pd.DataFrame(readable_prediction)
st.dataframe(new_df)
# In[14]:

#new_df['flags']=new_df[new_df.loc[0].str.contains("Outbreak|Pandemic")]
#outbreak = new_df.loc[0].str.contains("Outbreak|Pandemic")
#st.write(new_df)
#try:
 #   st.dataframe(flags)    
#except ValueError:
 #   st.write("no dice")
#def find_outbreak(data=new_df):

#try:
 #   outbreak_df = new_df.loc[0].str.contains("Outbreak|Pandemic")
  #  st.write("P")
#except (ValueError, NameError, TypeError):
 #   st.write("There are no outbreak for this period")
#else:
 #   st.write('aha!')
#return outbreak_df

#flags=find_outbreak()




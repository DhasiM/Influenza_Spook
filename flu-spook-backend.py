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
prophet=pickle.load(open('prophet.sav', 'rb'))
pro_regressor=pickle.load(open('prophet_pro.sav', 'rb'))


DATA_PATH='WPOFluNetInteractiveReport.csv'

@st.cache #cache results of function

def load_and_process_data(path=DATA_PATH):
    ''' 
    Returns a pre-processed dataframe and target
    
    This function reads the dataframe from the origin, parses it and pre-processes it.
    
        Parameters: 
            DATA_PATH is the url, path or name of the file to be loaded. Here it uses .csv but
            can be modified to accept tabular data of any format.
    
        Returns: Pandas dataframe loaded in memory and target column.
    '''
    data= pd.read_csv(path, parse_dates=['EDATE'], index_col='EDATE', skiprows=3)
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
    
        Parameters: 
            data: pre-loaded dataframe.
    
        Returns: 
            data: reduced dataframe with only the year of interest.
    
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
    Allows the user to select a country of interest from the dataframe
    
        Parameters: 
            data: pre-loaded dataframe or data output of _select_year
    
        Returns: 
            data: reduced dataframe with only the country of interest.
    
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
            
    user_year=int(st.sidebar.text_input("Enter year", 0))
    if user_year != 0:
        try:
            data=select_year(data, year=int(user_year))
            start_date=user_year
            end_date= user_year+1
                #data, target = process_selection(data)
            st.write('You have selected data for', user_country, 'for the year', user_year)
            st.dataframe(data.tail(5))
        except KeyError:
            st.write('No data for that year')
        except TypeError:
            st.write('Enter a valid year')
elif user_country == 'None':
    start_date=min(data.Year)
    end_date= max(data.Year)

if user_country == 'None':
    user_year = int(st.sidebar.text_input("Filter by year only", 0))   
    if user_year !=0 :   
        data=select_year(data, year=int(user_year))
                #data, target = process_selection(data)
        start_date=user_year
        end_date= user_year+ 1

        st.write('You have selected data for the year', user_year)
        st.dataframe(data.tail(5))




    

        
@st.cache
def prophet_prediction(data=data, period=2):
    '''
    Runs influenza incidence prediction
    
        Parameters: 
            data: pre-loaded dataframe or data output of _select_year or select_country
            period: number of weeks to looks ahead, default is set to 2 weeks
    
        Returns: 
            future_data= future dates as determined by prophet
            forecast_data: dataframe of prophet predcitons which include prediction, upper and lower limits.
    
    '''
    #data, target=process_selection()
    cat_data = pd.get_dummies(data)
    prophet_df=cat_data.reset_index()
    prophet_df.rename(columns = {'EDATE':'ds', 'ALL_INF':'y'}, inplace = True)
    # prepare expected column names
    data= prophet_df
    data['ds']= pd.to_datetime(data['ds'])
    data.sort_values(by='ds', axis=0, ascending=True, inplace=True)
    future_data = prophet.make_future_dataframe(periods=14)

#forecast the data for Test  data
    forecast_data = prophet.predict(future_data)
    prophet.plot(forecast_data)
    return forecast_data, future_data

data_load_state = st.text('Please wait as forcasting model runs...')

period=int(st.sidebar.text_input("How many weeks ahead do you want to forecast?", 2))
if period != 2:
    forecast_data, future_data =prophet_prediction(data, period)
else:
    forecast_data, future_data =prophet_prediction()

data_load_state.text("Forecast complete!")

#st.dataframe(future_data.head(5))
#def plot_forecast(forecast_data):
 #   model.plot(forecast_data)

st.subheader('Forecast influenza data')

  
if st.sidebar.button('See prophet model graph'):
    plot=prophet.plot(forecast_data)
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



df=data.reset_index()


#@st.cache   
#def compare_influenza_incidence(data=data):
 #   '''
  #  Compare the incidence of pandemic prone influenza A and endemic Influenza B viruses
    
   #     Parameters: 
    #        data: pre-loaded dataframe or data output of _select_year r select_country
    
     #   Returns: 
      #      fig= an interactive plotly scatter plot of influenza subtype incidence.
    
   # '''
    
    #df=data.reset_index()
    #fig =px.scatter(df, x='EDATE',y=['ALL_INF', 'INF_A', 'INF_B'])
#    return fig
#fig =px.scatter(x=df.EDATE,y=[df.ALL_INF,forecast_data.yhat])


#@st.cache(suppress_st_warning=True)
if st.button('Compare influenza subtype incidence'):
    #fig =  compare_influenza_incidence()
    fig =px.scatter(df, x='EDATE',y=['ALL_INF', 'INF_A', 'INF_B'])

    st.plotly_chart(fig)
  #  st.pyplot(fig)
    

@st.cache   
def outbreak_predictions(forecast_data=forecast_data):
    '''
    
     Classifies disease level of predictions
    
        Parameters: 
                    forecast_data: output of prophet prediction
        Returns:
                    readable_prediction: list of classified predictions in text
                    
    '''
    
    
    preds = outbreak.predict(forecast_data.yhat.array.reshape(-1, 1))
    labelencoder = LabelEncoder()#one hot encode the categores from label encoder
    # using the encoder to encode the categorical columns
    Y= labelencoder.fit_transform(target)
    readable_prediction=labelencoder.inverse_transform(preds)
    #y2 =
    return readable_prediction

readable_prediction= outbreak_predictions()
reads=pd.DataFrame(columns = ['preds']) 
reads.preds= pd.Series(readable_prediction)
#reads.rename(columns ={'0':'preds'}, inplace=True)
new_df=pd.merge(forecast_data, reads, left_index=True, right_index=True)
#pred= pd.DataFrame(readable_prediction)
#st.dataframe(new_df)

import re
def get_outbreak_alert(df=new_df):
    '''
    
    Creates a list of predicted dates with outbreaks
    
        Parameters: 
                    df: data frame of predictions and forecast dates
        Returns:
                    outbreaks: list of unique dates for potential outbreaks
                    
    '''
    df['level']= df.preds.str.contains(pat='outbreak',flags=re.IGNORECASE, regex=True)
    outbreaks = df[(df.level == True)]
    outbreaks=outbreaks.ds.dt.strftime('%Y-%m-%d')
    outbreaks = outbreaks.unique()
    
    outbreaks=outbreaks.tolist()
    return outbreaks

outbreaks =get_outbreak_alert()

if len(outbreaks) == 0:
    st.write("There are no outbreaks forecasted for the selected period")
else:
    st.write("There is a chance of an outbreak for the above dates")





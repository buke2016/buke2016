import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
%matplotlib inline

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")


def load_data():
    daily_new_cases = None

    covid_df = pd.read_csv('assets/time_series_covid19_confirmed_global.csv')
#     print(covid_df.head())

    #try melting
    covid_melty = pd.melt(covid_df, id_vars = ['Country/Region', 'Province/State'], value_vars = covid_df.columns[4:],
                      var_name = 'Date', value_name = 'Cumulative_Cases')
#     print(covid_melty.tail(5))


    #try to group by date, then later take the diff of each column before...
    covid_groupdate = covid_melty.groupby('Date').sum().reset_index()
#     print(covid_groupdate.head())

    #Create a column that converts every Date string into a pd.DatetimeIndex, then set this as the index and drop the old
    #Date column
    covid_groupdate['Date_Time'] = pd.to_datetime(covid_groupdate['Date'])
    covid_groupdate.sort_values(by='Date_Time',inplace = True)
    covid_groupdate.drop('Date', axis = 1, inplace = True)
    covid_groupdate.set_index('Date_Time', inplace = True)
#     covid_groupdate.head()

    #Take the difference between every day its respective next day.
    #Rename the column to New cases as calculated be .diff()
    #Drop NA rows. The top row after running .diff() is always NA as there was no day before it
    covid_new_cases = covid_groupdate.diff()
    covid_new_cases.rename(columns = {'Cumulative_Cases':'New_Cases'}, inplace=True)
    covid_new_cases.dropna(inplace=True)
#     covid_new_cases


    daily_new_cases = covid_new_cases['New_Cases']


    return daily_new_cases





from statsmodels.tsa.seasonal import seasonal_decompose, DecomposeResult

def sea_decomp(ser, model="additive"):
    """
    Takes in a series and a "model" parameter indicating which seasonal decomp to perform
    """
    result = None

    # YOUR CODE HERE
    result = seasonal_decompose(ser,model = model)

    return result





from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def fit_trend(ser, n):
    """
    Takes a series and fits an n-th order polynomial to the series.
    Returns the predictions.
    """
    #Generate ordinal values to represent timestamps for use in regression
    # Create train_X and train_y
#     train_X, train_y = np.asarray(ser.index.map(dt.datetime.toordinal)), np.asarray(ser) # xi's and yi's
    train_X, train_y = np.asarray([i+1 for i in range(len(ser.index))]), np.asarray(ser)

    # Fit a polynomial regression model - code given to you

    train_X = PolynomialFeatures(n).fit_transform(train_X.reshape(-1, 1))

    lin_reg = LinearRegression().fit(train_X, train_y.reshape(-1))

    # Make predictions to create the trend curve
    # YOUR CODE HERE
    y_pred = np.asarray(lin_reg.predict(train_X))

    trend_curve = y_pred

    return trend_curve




def calc_wma(ser, wd_size, weights=1):
    """
    Takes in a series and calculates the WMA with a window size of wd_size
    """
    wma = []
    #Set the number of weights to the window size
#     weights = np.arange(1, wd_size+1, 1)
    weights = np.arange(wd_size, 0, -1)
    print(weights)


    if isinstance(weights, int):
        weights = np.full(wd_size, weights)

    assert len(weights) == wd_size, "Q4: The size of the weights must be the same as the window size. "

    # YOUR CODE HERE

    ser_len = len(ser)
    for i in range(1, ser_len+1):
        if i >= wd_size:
#             print("i", i)
            temp_window = ser[i-wd_size:i]
            #resort the weights so they line up in the j loop such that the greatest weight goes with the most recent observ.
            new_weights = np.sort(weights)
#             print(new_weights)
#             print(temp_window)

            adjusted_vals = []
            for j in range(len(temp_window)):
                weighted_val = temp_window[j] * new_weights[j]
                adjusted_vals.append(weighted_val)

            new_val = sum(adjusted_vals)/sum(weights)

            wma.append(new_val)

        else:
            print("i", i)
            new_weights = weights[:i]
            #resort the weights so they line up in the j loop such that the greatest weight goes with the most recent observ.
            new_weights = np.sort(new_weights)
#             print(new_weights)
            temp_window = ser[:i]
#             print(temp_window)

            adjusted_vals = []
            for j in range(len(temp_window)):
                weighted_val = temp_window[j] * new_weights[j]
                adjusted_vals.append(weighted_val)

            new_val = sum(adjusted_vals)/sum(new_weights)

            wma.append(new_val)

    wma = np.asarray(wma)
#     print(len(wma))
#     print(len(ser))
    return wma
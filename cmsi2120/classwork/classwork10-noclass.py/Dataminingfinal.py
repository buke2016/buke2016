import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Set pandas options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

# Ensure matplotlib plots are displayed in the Jupyter notebook
# %matplotlib inline for jupyter notebook
register_matplotlib_converters()


def load_data():
    covid_df = pd.read_csv('assets/time_series_covid19_confirmed_global.csv')

    covid_melty = pd.melt(covid_df, id_vars=['Country/Region', 'Province/State'],
                          value_vars=covid_df.columns[4:],
                          var_name='Date', value_name='Cumulative_Cases')

    covid_groupdate = covid_melty.groupby('Date').sum().reset_index()
    covid_groupdate['Date_Time'] = pd.to_datetime(covid_groupdate['Date'])
    covid_groupdate.set_index('Date_Time', inplace=True)

    covid_new_cases = covid_groupdate.diff()
    covid_new_cases.rename(columns={'Cumulative_Cases': 'New_Cases'}, inplace=True)
    covid_new_cases.dropna(inplace=True)

    daily_new_cases = covid_new_cases['New_Cases']

    return daily_new_cases


def sea_decomp(ser, model="additive"):
    result = seasonal_decompose(ser, model=model)
    return result


def fit_trend(ser, n):
    train_X = np.arange(1, len(ser) + 1).reshape(-1, 1)
    train_X = PolynomialFeatures(n).fit_transform(train_X)

    lin_reg = LinearRegression().fit(train_X, ser)

    y_pred = lin_reg.predict(train_X)

    trend_curve = y_pred

    return trend_curve


def calc_wma(ser, wd_size, weights=1):
    wma = []

    if isinstance(weights, int):
        weights = np.full(wd_size, weights)

    assert len(weights) == wd_size, "The size of the weights must be the same as the window size."

    ser_len = len(ser)

    for i in range(1, ser_len + 1):
        if i >= wd_size:
            temp_window = ser[i - wd_size:i]
            new_weights = np.sort(weights)

            adjusted_vals = temp_window * new_weights
            new_val = np.sum(adjusted_vals) / np.sum(weights)

            wma.append(new_val)
        else:
            new_weights = weights[:i]
            new_weights = np.sort(new_weights)
            temp_window = ser[:i]

            adjusted_vals = temp_window * new_weights
            new_val = np.sum(adjusted_vals) / np.sum(new_weights)

            wma.append(new_val)

    wma = np.asarray(wma)

    return wma


# Example usage of the functions:
if __name__ == "__main__":
    daily_new_cases = load_data()
    decomposition_result = sea_decomp(daily_new_cases)
    trend_curve = fit_trend(daily_new_cases, n=2)
    weighted_moving_average = calc_wma(daily_new_cases, wd_size=7, weights=[1, 2, 3, 4, 5, 6, 7])

    # Plot the results
    plt.figure(figsize=(12, 8))

    # Plot daily new cases
    plt.subplot(3, 1, 1)
    plt.plot(daily_new_cases, label='Daily New Cases')
    plt.title('Daily New Cases')
    plt.legend()

    # Plot trend curve
    plt.subplot(3, 1, 2)
    plt.plot(trend_curve, label='Trend Curve', color='orange')
    plt.title('Trend Curve')
    plt.legend()

    # Plot weighted moving average
    plt.subplot(3, 1, 3)
    plt.plot(weighted_moving_average, label='Weighted Moving Average', color='green')
    plt.title('Weighted Moving Average')
    plt.legend()

    plt.tight_layout()
    plt.show()


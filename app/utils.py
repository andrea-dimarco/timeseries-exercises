import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import statsmodels.formula.api as smf




def get_normal_data(n_samples:int, mean:float=0.0, std:float=1.0, seed:int=0) -> pd.Series:
    '''
    Generate univariate time series data from normal distribution of provided eman and std
    '''
    np.random.seed(seed)
    return pd.Series(np.random.normal(loc=mean, scale=std, size=n_samples))



def get_linear_trend_normal_data(n_samples:int, mean:float=0.0, std:float=1.0, seed:int=0) -> pd.Series:
    '''
    Generate univariate time series data from normal distribution of provided eman and std
    '''
    np.random.seed(seed)
    data = np.random.normal(loc=mean, scale=std, size=n_samples) + np.arange(n_samples)*0.1
    return pd.Series(data)



def plot_timeseries(time_series:pd.Series, output_file:str) -> None:
    '''
    Plot the time series
    '''
    plt.figure(figsize=(10, 6))
    plt.plot(time_series)
    plt.title('Sample Time Series Data')
    plt.savefig(output_file)
    plt.clf()



def diagnostic_check(model, output_folder:str, verbose:bool=False) -> None:

    if verbose:
        print("Generatinf residual diagnostic check plots ... ", end="")
    # Plot the residuals
    residuals = model.resid
    plt.figure(figsize=(10, 6))
    plt.plot(residuals)
    plt.title('Residuals of the ARMA Model')
    plt.savefig(f"{output_folder}residuals.png")
    plt.clf()

    # Plot the ACF of the residuals
    plt.figure(figsize=(10, 6))
    sm.graphics.tsa.plot_acf(residuals, lags=30)
    plt.savefig(f"{output_folder}residuals_ACF.png")
    plt.clf()

    # Plot the PACF of the residuals
    plt.figure(figsize=(10, 6))
    sm.graphics.tsa.plot_pacf(residuals, lags=30)
    plt.savefig(f"{output_folder}residuals_PACF.png")
    plt.clf()

    if verbose:
        print("done.")



def forecast_expected_value(model, timeseries:pd.Series, n_periods:int) -> pd.Series:
    return model.predict(n_periods=n_periods, 
                         exogenous=timeseries,
                         return_conf_int=False)



def plot_forecast(time_series:pd.Series, forecast:pd.Series, output_folder:str, verbose:bool=False, model_name:str="ARIMA") -> None:
    # Plot the forecast
    plt.figure(figsize=(10, 6))
    plt.plot(time_series, label='Original')
    if len(time_series) != len(forecast):
        plt.plot(np.arange(len(time_series), len(time_series) + len(forecast)), forecast, label='Forecast')
    else:
        plt.plot(forecast, label='Forecast')
    # plt.fill_between(np.arange(len(time_series), len(time_series) + forecast_steps), conf_int[:, 0], conf_int[:, 1], color='pink', alpha=0.3)
    plt.title(f'{model_name} Model Forecast')
    plt.legend()
    plt.savefig(f"{output_folder}forecast.png")
    plt.clf()




if __name__ == '__main__':

    # parameters
    p:int = 2 # AR(p) order
    q:int = 1 # MA(q) order
    i:int = 1 # Diff order
    n_periods:int = 1
    n_samples:int = 100
    mean:float = 0.0
    std:float = 1.0
    output_folder:str = "/data/"
    verbose:bool = True


    data = get_linear_trend_normal_data(n_samples=n_samples, mean=mean, std=std)
    plot_timeseries(time_series=data, output_file=f"{output_folder}timeseries.png")

    # Fit the ARMA model
    model = tsa.ARIMA(endog=data, order=(p, i, q)).fit()

    if verbose:
        print(model.summary())

    diagnostic_check(model=model, output_folder=f"{output_folder}residuals/", verbose=verbose)

    forecast = forecast_expected_value(model=model, timeseries=data, n_periods=n_periods)
    plot_forecast(time_series=data, forecast=forecast, output_folder=output_folder, verbose=verbose)



    
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import matplotlib.pyplot as plt



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


def plot_series(time_series:pd.Series, output_file:str) -> None:
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



def forecast_expected_value(model, forecast_steps) -> pd.Series:
    
    mu_hat = model.forecast(steps=forecast_steps)

    return mu_hat



def plot_forecast(time_series:pd.Series, forecast:pd.Series, output_folder:str, verbose:bool=False) -> None:
    # Plot the forecast
    plt.figure(figsize=(10, 6))
    plt.plot(time_series, label='Original')
    plt.plot(np.arange(len(time_series), len(time_series) + forecast_steps), forecast, label='Forecast')
    # plt.fill_between(np.arange(len(time_series), len(time_series) + forecast_steps), conf_int[:, 0], conf_int[:, 1], color='pink', alpha=0.3)
    plt.title('ARMA Model Forecast')
    plt.legend()
    plt.savefig(f"{output_folder}forecast.png")
    plt.clf()

if __name__ == '__main__':

    # parameters
    p:int = 1
    q:int = 0
    i:int = 1
    forecast_steps:int = 100
    n_samples:int = 100
    mean:float = 0.0
    std:float = 1.0
    output_folder:str = "/data/"
    verbose:bool = True


    data = get_linear_trend_normal_data(n_samples=n_samples, mean=mean, std=std)
    plot_series(time_series=data, output_file=f"{output_folder}timeseries.png")

    # Fit the ARMA model
    arma_model = tsa.ARIMA(data, order=(p, i, q)).fit()

    if verbose:
        print(arma_model.summary())

    diagnostic_check(model=arma_model, output_folder=output_folder, verbose=verbose)

    forecast = forecast_expected_value(model=arma_model, forecast_steps=forecast_steps)
    plot_forecast(time_series=data, forecast=forecast, output_folder=output_folder, verbose=verbose)
    
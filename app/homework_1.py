import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

import statsmodels.api as sm
import statsmodels.tsa.api as tsa
import statsmodels.formula.api as smf

from ar import AR
from ipopt import IPOPT
import utils




def get_data_ar(n_samples:int,
                coefficients:list[float],
                offset:float=0.0,
                mean:float=0.0,
                std:float=1.0,
                seed:int=0
               ) -> pd.Series:
    '''
    Generate univariate time series data from normal distribution of provided eman and std
    '''
    np.random.seed(seed=seed)
    
    model:AR = AR(p=len(coefficients), c=offset, mu=mean, std=std)
    initial_state:list[float] = [0.0 for _ in range(len(coefficients))]

    model.state(initial_state)
    model.phi(coefficients)

    Y:list[float] = list()
    for _ in range(n_samples):
        yt = model.run()
        model.push_state(yt)
        Y.append(yt)

    return pd.Series(Y)



def mse_loss(xdict:dict[str,list[float]], saturation:float=10000000) -> tuple[dict[str,float], bool]:
    # GET VARIABLES
    PHI = xdict["PHI"]
    
    # OBJECTIVE FUNCTION
    funcs:dict = dict()
    obj:float = 0.0
    forecasts:list[float] = list()

    model.phi(new_phi=PHI)
    p:int = model.p()
    current_idx:int = 0

    for sample in timeseries:
        if current_idx < p:
            current_idx += 1
            model.push_state(sample)
            continue
        pred = model.run()
        obj += (sample - pred)**2
        model.push_state(sample)

    # FORMAT RESULTS
    if ((not np.isnan(obj)) or (obj < saturation)):
        fail = False
    else:
        fail = True
    funcs["OBJ"] = obj
    return funcs, fail



if __name__ == '__main__':

    # parameters
    seed:int = 0
    offset:float = 0.0
    phi_list:list[float] = [ 0.3, 0.3, 0.3 ]
    
    p = len(phi_list)
    initial_state:list[float] = [0.0 for _ in range(p)]

    n_periods:int = 1
    n_samples:int = 1000
    mean:float = 0.0
    std:float = 1.0
    output_folder:str = "/data/homework01/"
    verbose:bool = True

    # get data
    timeseries:pd.Series = get_data_ar(n_samples=n_samples,
                                       coefficients=phi_list,
                                       offset=offset,
                                       mean=mean,
                                       std=std,
                                       seed=seed,
                                      )
    
    utils.plot_timeseries(time_series=timeseries, output_file=f"{output_folder}target_timeseries.png")

    model:AR = AR(p=p, c=offset, mu=mean, std=std)
    model.state(new_state=initial_state)

    # Estimate model
    optimizer = IPOPT(obj_function=mse_loss, problem_name="AR Estimation", quiet=False)
    optimizer.add_var_group(name="PHI", n_vars=p, lower=0.0)
    optimizer.solve()
    sol = optimizer.solution()



    
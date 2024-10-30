import pdb
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from astropy.timeseries import LombScargle
from actiPy import periodogram

# directories 
pir_dir = Path(
    "/Users/angusfisk/Documents/01_personal_files/01_work/"
    "11_LL_paper/02_analysis/01_data_files/10_pirfiles"
)
pir_files = list(pir_dir.glob("*.csv"))
curr_file = pir_files[0]

# read in data for all animals
ll_dfs = []
for curr_file in pir_files:
    
    pir_data = pd.read_csv(curr_file, index_col=0, parse_dates=True)

    # clean data, removing unused columns 
    unused_cols = list(pir_data.columns[i] for i in [0, 5, 6, 8])
    pir_data_clean = pir_data.drop(unused_cols, axis=1)
    pir_data_clean.index = pir_data.index.tz_localize(None)
    pir_data_clean = pir_data_clean.resample('10s').mean()
    
    # select just the LL bit 
    ll_start = pd.to_datetime("2018-04-10 07:00:00")
    ll_end = pd.to_datetime("2018-04-25 07:00:00")
    ll_data = pir_data_clean.loc[ll_start:ll_end]
   

    ll_dfs.append(ll_data)

all_data = pd.concat(ll_dfs)


# run period estimation (MESA)
curr_data = ll_data.iloc[:, 3]

# periods = periodogram.get_period(ll_data)
period_list = []
hr_range = ["19h", "26h"]
for no, curr_data in enumerate(ll_data):
    period_times = periodogram._period_df(
        ll_data, 
        animal_no=no,
        low_time=hr_range[0],
        high_time=hr_range[1]
    )
    fig, ax = plt.subplots()
    ax.plot(period_times.index.get_level_values(1), period_times.values)
    fig.show()
    period_index = np.argmax(period_times)
    period = (period_times.iloc[period_index].name[1]).total_seconds() / 3600
    period_list.append(period)
        
# save results 

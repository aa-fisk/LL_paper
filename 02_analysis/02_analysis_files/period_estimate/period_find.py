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
hr_range = ["19h", "26h"]

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
    
    # set correct column names for concat
    if curr_file.stem == 'EEG_1':
        col_names = ["LL1", "LL2", "LL3", "LL4", "LDR"]
    else:
        col_names = ["LL5", "LL6", "LL7", "LL8", "LDR"]
    ll_data.columns = col_names

    ll_dfs.append(ll_data)

all_data = pd.concat(ll_dfs, axis=1, join='inner')


# calculate period for all animals 
period_list = []
for no, curr_data in enumerate(all_data):
    print(no)
    period_times = periodogram._period_df(
        all_data, 
        animal_no=no,
        low_time=hr_range[0],
        high_time=hr_range[1],
        drop_level=False
    )
#    fig, ax = plt.subplots()
#    ax.plot(period_times.index.get_level_values(1), period_times.values)
#    fig.show()
    period_index = np.argmax(period_times)
    period = (period_times.iloc[period_index].name[1]).total_seconds() / 3600
    period_list.append(period)
        

# why not working? 
# create x and y values of observations
data = all_data
animal_no = 0
base_time = "10s"
low_time = hr_range[0]
high_time = hr_range[1]
base_unit = "s"

time = np.linspace(0, len(data), len(data))
y = data.iloc[:, animal_no].values

# convert all times into the same units (seconds)
base_secs = pd.Timedelta(base_time).total_seconds()
low_secs = pd.Timedelta(low_time).total_seconds()
high_secs = pd.Timedelta(high_time).total_seconds()

# frequency is number of 1/ cycles per base = base / cycles
low_freq = base_secs / low_secs
high_freq = base_secs / high_secs
frequency = np.linspace(high_freq, low_freq, 1000)

# find the LombScargle power at each frequency point
power = LombScargle(time, y).power(frequency)



# save results 

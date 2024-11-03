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
save_name = pir_dir.parent / "12_periods.csv"
pir_files = list(pir_dir.glob("*.csv"))
hr_range = ["19h", "26h"]
ll_start = pd.to_datetime("2018-04-10 07:00:00")
ll_end = pd.to_datetime("2018-04-25 07:00:00")

# read in data for all animals
ll_dfs = []
for curr_file in pir_files:

    pir_data = pd.read_csv(curr_file, index_col=0, parse_dates=True)

    # clean data, removing unused columns
    unused_cols = list(pir_data.columns[i] for i in [0, 5, 6, 8])
    pir_data_clean = pir_data.drop(unused_cols, axis=1)
    pir_data_clean.index = pir_data.index.tz_localize(None)
    pir_data_resampled = pir_data_clean.resample('10s').mean()
    pir_data_resampled = pir_data_resampled.interpolate()

    # select just the LL bit
    ll_data = pir_data_resampled.loc[ll_start:ll_end]

    # set correct column names for concat
    if curr_file.stem == 'EEG_1':
        col_names = ["LL1", "LL2", "LL3", "LL4", "LDR"]
    else:
        col_names = ["LL5", "LL6", "LL7", "LL8", "LDR"]
    ll_data.columns = col_names

    ll_dfs.append(ll_data)

all_data = pd.concat(ll_dfs, axis=1, join='inner')


# calculate period for all animals
period_times = [
    periodogram._period_df(
        all_data,
        animal_no=x,
        low_time=hr_range[0],
        high_time=hr_range[1],
        drop_level=False
    ) for x in range(len(all_data.columns))
]

# convert into hours
period_dict = {}
for i, curr_period in enumerate(period_times):
    period_index = np.argmax(curr_period)
    period = (curr_period.iloc[period_index].name).total_seconds() / 3600
    period_dict[all_data.columns[i]] = period

period_df = pd.DataFrame.from_dict(period_dict, orient='index')
period_df.to_csv(save_name)

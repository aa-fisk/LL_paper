import pdb
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from pathlib import Path

# Parameters
fft_dir_path = Path(
    '/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/'
    '02_analysis/01_data_files/07_clean_fft_files/01_script/fro'
)
freq_range = [0.5, 4]


# get list of files 
files = list(fft_dir_path.glob('LL6*'))
curr_file = files[0]

# read in data 
data = pd.read_csv(
    curr_file, index_col=[0, -1], parse_dates=True
).sort_index().xs("fro", level=1)


# calculate delta power 

# make columns numbers so easy to handle 
freq_df = data.drop("State", axis=1)
freq_df.columns = pd.to_numeric(freq_df.columns)

# calculate power in delta 
delta_range = freq_df.loc[:, freq_range[0]:freq_range[1]]
delta_power = delta_range.sum(axis=1)


# Create a figure for plotting with shared x-axis
num_days = len(delta_power.groupby(delta_power.index.date))
fig, axs = plt.subplots(num_days, 1, sharex=True, figsize=(12, 8))

# Group by day for plotting
daily_groups = delta_power.groupby(delta_power.index.date)

# Create subplots for each day
for idx, (day, group) in enumerate(daily_groups):
    axs[idx].plot(group.index, group.values, color='b')
    axs[idx].grid()
    axs[idx].set_title(
        f'Delta Power Time Course for {day}'
    )  # Optional title for context

# Remove x-ticks and set labels for the shared x-axis
for ax in axs:
    ax.label_outer()  # Only show outer labels

plt.tight_layout()
plt.show()# colour by vigilance state

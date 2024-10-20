import pdb
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set_theme()
from pathlib import Path

# Parameters
fft_dir_path = Path(
    '/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/'
    '02_analysis/01_data_files/07_clean_fft_files/01_script/fro'
)
save_dir_path = fft_dir_path.parents[3] / "03_analysis_outputs" \
        / "06_explore"
freq_range = [0.5, 4]
state_col = "State"
channel_col = "Channel" 

# get list of files 
files = list(fft_dir_path.glob('LL1*'))
curr_file = files[0]

# read in data 
data = pd.read_csv(
    curr_file, index_col=0, parse_dates=True
).sort_index()

# get the current day
unique_dates = pd.Series(data.index.date).unique()
curr_day = unique_dates[8]

def plot_delta_power_for_day(
        data, 
        curr_day, 
        state_col, 
        channel_col,
        save_dir_path, 
        curr_file,
        freq_range=[0.5, 4],
        show=False,
        save=False):

    # calculate delta power 
        # make columns numbers so easy to handle 
    freq_df = data.drop([state_col, channel_col], axis=1)
    freq_df.columns = pd.to_numeric(freq_df.columns)
        # calculate power in delta 
    delta_range = freq_df.loc[:, freq_range[0]:freq_range[1]]
    delta_power = delta_range.sum(axis=1)

    # select just the current day 
    delta_power_curr_day = delta_power.loc[
        delta_power.index.date == curr_day
    ] 
    state_curr_day = data.loc[
        delta_power.index.date == curr_day, state_col
    ]

    # Add in the correct state labels 
    delta_power_curr_day = pd.concat(
        [delta_power_curr_day, state_curr_day], axis=1
    )


    # Plot each state separately on the same axis 
    fig, axs = plt.subplots()

    for state, group in delta_power_curr_day.groupby(state_col):
        # Drop the state column before resampling
        curr_state_data = group.drop(columns=[state_col])

        # Resample and fill missing values with 0s
        resampled_data = curr_state_data.resample("4s").mean().fillna(0)

        # Plot the resampled data
        axs.plot(
            resampled_data.index, resampled_data[0], label=state  
            # resampled delta_power
        )

    if show :
        plt.show()

    if save : 
        # save 
        save_name = str(curr_day) + "-" + curr_file.stem + ".png"
        fig.savefig(str(save_dir_path / save_name))
    plt.close(fig)


plot_delta_power_for_day(
    data, curr_day, state_col, channel_col, save_dir_path, curr_file,
    show=True, save=False
)



import pdb
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
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


def plot_delta_power_for_day(
        data, 
        curr_day, 
        state_col, 
        channel_col,
        save_dir_path, 
        curr_file,
        freq_range=[0.5, 4],
        showfig=False,
        savefig=False):

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

    # Define state order and convert state_col to categorical
    state_order = ['awake', 'non-REM', 'REM']
    
    # Check for case sensitivity and unexpected values
    delta_power_curr_day[state_col] = pd.Categorical(
        delta_power_curr_day[state_col].astype(str).str.strip(),
        categories=state_order,
        ordered=True
    )

    # Plot each state separately on the same axis 
    fig, axs = plt.subplots(figsize=(11.69, 8.27))

    # Set the x-axis limits for midnight to midnight of the current day
    start_time = pd.Timestamp(curr_day)
    end_time = start_time + pd.Timedelta(days=1)
    axs.set_xlim(start_time, end_time)

    # Format x-axis to show hour and minute
    axs.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    
    # Set the ylim 
    axs.set_ylim([0, 4e5])

    for state, group in delta_power_curr_day.groupby(state_col):
       
        if group.empty:  # Check if group is empty
            print(f"Warning: Group for state '{state}' is empty.")
            continue  # Skip empty groups

        # Drop the state column before resampling
        curr_state_data = group.drop(columns=[state_col])

        # Resample and fill missing values with 0s
        resampled_data = curr_state_data.resample("4s").mean().fillna(0)

        # Plot the resampled data
        axs.plot(
            resampled_data.index, resampled_data[0], label=state  
            # resampled delta_power
        )
            
    # Add labels and title
    axs.set_xlabel('Time')
    axs.set_ylabel('Delta Power')
    axs.set_title(f'Delta Power by State for {curr_file.stem} {curr_day} ')
    axs.legend(title='State')
    axs.grid(True)
    plt.xticks(rotation=45)

    if showfig :
        plt.show()
    
    if savefig : 
        # save 
        save_name = curr_file.stem + "_" +  str(curr_day) + ".png"
        fig.savefig(str(save_dir_path / save_name))
    plt.close(fig)

def plot_delta_power_all_days(
        data,
        save_dir_path,
        curr_file,
        state_col = "State",
        channel_col = "Channel", 
        freq_range=[0.5, 4],
        **kwargs):

    # get the current day
    unique_dates = pd.Series(data.index.date).unique()
    
    for curr_day in unique_dates:
        plot_delta_power_for_day(
            data, curr_day, state_col, channel_col, save_dir_path, curr_file,
            **kwargs
        )



if __name__ == "__main__":
   
    # get list of files 
    files = list(fft_dir_path.glob('*.csv'))
    
    for curr_file in files:
        # read in data 
        data = pd.read_csv(
            curr_file, index_col=0, parse_dates=True
        ).sort_index()
       
        # plot all days for current animal 
        plot_delta_power_all_days(
            data,
            save_dir_path,
            curr_file,
            showfig=False,
            savefig=True
        )

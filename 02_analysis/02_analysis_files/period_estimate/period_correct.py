import pdb
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# files and dirs 
derivation = "fro"
import_dir = Path(
    "/Users/angusfisk/Documents/01_personal_files/01_work/"
    "11_LL_paper/02_analysis/01_data_files/07_clean_fft_files/01_script"
) / derivation
period_file = list(import_dir.parents[2].glob("*periods*"))
save_dir = import_dir.parent / "02_corrected" / derivation
files = list(import_dir.glob("*.csv"))

# constants 
ll_start = pd.to_datetime("2018-04-10 07:00:00")
ll_end = pd.to_datetime("2018-04-25 07:00:00")

curr_file = files[1] # make sure not LL8
# read in periods 


#re-indexing based on new frequency 

def process_period_data(
        data,
        base_freq = 4,
        period = 24):

        
    # calculate what new frequency is 
    freq_ratio = 24 / curr_period
    new_freq = base_freq * freq_ratio
    new_freq_str = str(np.round(new_freq * 1000))+ "ms"

    # create new index based on this 
    start_time = data.index[0]
    data_length = len(data)
    new_index = pd.date_range(
        start=start_time, 
        periods=data_length, 
        freq=new_freq_str
    )

    # reindex the data 
    reindexed_data = pd.DataFrame(
        data=data.values, 
        index=new_index,
        columns=data.columns
    )

    return reindexed_data

# process all the files
if __name__ == "__main__":
    
    # read in periods 
    periods = pd.read_csv(period_file[0], index_col=0)

    # read in fft data 
    for curr_file in files: 
        data = pd.read_csv(
            curr_file, index_col=0, parse_dates=True
        ).sort_index()
        data_ll = data.loc[ll_start:ll_end]
        curr_period = periods.loc[curr_file.stem].values[0]

        # save the data 

        


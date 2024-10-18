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

files = list(fft_dir_path.glob('LL4*'))
curr_file = files[0]

# read in data 
data = pd.read_csv(
    curr_file, index_col=[0, -1], parse_dates=True
).sort_index()
#data = pd.read_csv(curr_file, index_col=[0,1])
#for sleepsign fft files, header=17, skipfooter=(64825 - 2162))


fft_data = data.xs("fro", level=1)

# resample so can actually plot 
fft_data_resample = fft_data.drop("State", axis=1).resample("1min").mean()

# try plotting 
fig, ax = plt.subplots()

ax.plot(fft_data_resample.iloc[:, 0])

plt.show()




# code for checking clean auto fft 



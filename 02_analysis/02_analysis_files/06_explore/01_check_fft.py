import pdb
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from pathlib import Path

# Parameters
fft_dir_path = Path('/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/07_clean_fft_files/01_script')
channels = ['fro', 'occ', 'foc']  # Example channel names

files = list(fft_dir_path.glob('*.csv'))
curr_file = files[0]

# read in data 
data = pd.read_csv(curr_file, index_col=[-1, -2, -3])

fro_data = data.xs("fro", level="Channel")

plot_data = fro_data.reset_index(level=1, drop=True).drop("State", axis=1)


fig, ax = plt.subplots()

ax.plot(plot_data.iloc[:, 0])

plt.show()


import pdb
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from memspectrum import MESA

# directories 
pir_dir = Path(
    "/Users/angusfisk/Documents/01_personal_files/01_work/"
    "11_LL_paper/02_analysis/01_data_files/10_pirfiles"
)
pir_files = list(pir_dir.glob("*.csv"))
curr_file = pir_files[0]


# import PIR data
pir_data = pd.read_csv(curr_file, index_col=0, parse_dates=True)

# clean data, removing unused columns 
unused_cols = list(pir_data.columns[i] for i in [0, 5, 6, 8])
pir_data_clean = pir_data.drop(unused_cols, axis=1)
pir_data_clean.index = pir_data.index.tz_localize(None)

# select just the LL bit 
ll_start = pd.to_datetime("2018-04-10 07:00:00")
ll_end = pd.to_datetime("2018-04-25 07:00:00")
ll_data = pir_data_clean.loc[ll_start:ll_end]

# run period estimation (MESA)
curr_data = ll_data.iloc[:, 3]

def get_period_MESA(curr_data, hr_range = [19,26], figshow=False):
    m = MESA()
    m.solve(curr_data)

    # define frequencies to use 
    lower_hz = hr_range[0]/(60*60)  
    upper_hz = hr_range[1]/(60*60) 
    test_freq = np.linspace(upper_hz, lower_hz, 10000)  

    density_values = m.spectrum(dt=10, frequencies=test_freq)

    # Find the main frequency (peak in the power spectrum)
    main_frequency_index = np.argmax(density_values)
    main_frequency = test_freq[main_frequency_index]
    main_period = main_frequency * (60*60)
   
    if figshow:
        fig, ax = plt.subplots(2)

        ax[0].loglog((test_freq * (60*60)), density_values)
        ax[1].plot(curr_data)

        fig.show()

    return main_period

period_list = []
for col in ll_data:
    curr_data = ll_data.loc[:, col] 
    curr_period = get_period_MESA(curr_data, figshow=True)
    period_list.append(curr_period)



# save results 

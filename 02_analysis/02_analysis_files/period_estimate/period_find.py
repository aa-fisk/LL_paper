import pdb
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

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

# save results 

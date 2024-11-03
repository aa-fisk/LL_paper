from clean_auto_fft import load_annotations, convert_annotations_to_time_index
import pdb
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
sys.path.append(
    os.path.dirname(os.path.abspath(os.getcwd())) + '/01_preprocessing'
)


# Parameters
clean_fft_dir_path = Path(
    '/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/'
    '02_analysis/01_data_files/07_clean_fft_files/01_script/fro'
)
raw_fft_dir_path = clean_fft_dir_path.parents[2] / "06_fft_files" / "01_script"
states_dir_path = clean_fft_dir_path.parents[2] / "11_somnotate" \
    / "02_auto_states"

curr_anim = "LL4"
clean_files = list(clean_fft_dir_path.glob(f'{curr_anim}*'))
raw_files = list(raw_fft_dir_path.glob(f'{curr_anim}*'))
states_files = list(states_dir_path.glob(f'{curr_anim}*'))

curr_file_clean = clean_files[0]
curr_file_raw = raw_files[0]
curr_file_states = states_files[0]

# read in clean and raw file
clean_data = pd.read_csv(
    curr_file_clean, index_col=[0], parse_dates=True
).sort_index()

# raw_data = pd.read_csv(curr_file_raw, index_col=[0,1])
states_raw = load_annotations(curr_file_states)
states_converted = convert_annotations_to_time_index(
    states_raw,
    window_length=4,
    file_stem=curr_file_states.stem
)

pdb.set_trace()

# select the same day
day = pd.to_datetime(curr_file_raw.stem[-6:], yearfirst=True)
clean_day = clean_data.loc[str(day.date())]


# compare annotations

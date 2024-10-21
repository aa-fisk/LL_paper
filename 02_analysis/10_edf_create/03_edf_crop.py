import os
import pandas as pd
from pathlib import Path
from pyedflib import highlevel

# constants
ch_names = ['chan. 0', 'chan. 1', 'chan. 2', 'chan. 3']

# directories 
directory = Path(
    '/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper' 
    '02_analysis/01_data_files/01_edf/01_script'
)
state_dir = directory.parents[1] / '11_somnotate' / '05_visbrain' #annotations
save_dir = directory.parent / '02_cropped'

# get list of edf and annotations 
files = list(directory.glob('*.edf')) #raw_files 
state_files = list(state_dir.glob('*.hyp'))

# select only files with annotations 
# Create a mapping from base filenames to their corresponding state files
state_file_map = {file.stem: file for file in state_files}
# Select only files with annotations
filtered_edf_files = [file for file in files if file.stem in state_file_map]



# Iterate over files and corresponding annotations 
for file_test in filtered_edf_files:
    curr_state = state_file_map[file_test.stem]

    # read in file 
    signals, signal_headers, header = highlevel.read_edf(
            str(file_test), ch_names=ch_names
    )
    
    # read how long the file from header 
    curr_data = pd.read_csv(curr_state, sep='\t', header=None)
    duration = curr_data.iloc[0,1]
    print(file_test.stem) 
    print("Duration: {}".format(duration))
    print("Length of original data: {}".format(len(signals[0])/256))

    # crop signal to duration 
    day = int(256 * float(duration))
    signals_cropped = [arr[:day] for arr in signals]
    
    print("Length of cropped data: {}".format(len(signals_cropped[0])/256))

    # write file 
    save_name = save_dir / file_test.name
    highlevel.write_edf(str(save_name), signals_cropped, signal_headers, header)


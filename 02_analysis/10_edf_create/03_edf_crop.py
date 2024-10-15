import os
from pathlib import Path
from pyedflib import highlevel

day = 256 * 86400
ch_names = ['chan. 0', 'chan. 1', 'chan. 2', 'chan. 3']


# get list of files 
directory = Path('/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/01_edf/01_script')
files = list(directory.glob('*.edf'))
file_test = files[0]


for file_test in files: 
    # read in file 
    signals, signal_headers, header = highlevel.read_edf(str(file_test), ch_names=ch_names)

    # crop signals down to 24 hours 
    signals_cropped = [arr[:day] for arr in signals]

    # write file 
    save_dir = directory.parent / '02_cropped'
    save_name = save_dir / file_test.name
    highlevel.write_edf(str(save_name), signals, signal_headers, header)


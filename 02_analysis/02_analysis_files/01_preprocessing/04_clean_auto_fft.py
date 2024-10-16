import pdb
import pandas as pd
from pathlib import Path

# Parameters
annotation_file_path = Path('/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/11_somnotate/02_auto_states/LL1-EEG-EMG-180410.hyp')  # Replace with your annotation file path
fft_file_path = (annotation_file_path.parents[2] / '06_fft_files' / '01_script' / annotation_file_path.stem).with_suffix(".csv") 
sampling_rate = 256  # Sampling rate in Hz
window_length = 4  # Length of the window in seconds


# Load sleep state annotations
def load_annotations(file_path):
    # Assuming the annotations file has a single column for time points and a corresponding state
    annotations_df = pd.read_csv(file_path, delimiter='\t', skiprows=2, header=None, names=['State','Time'])

    # Convert 'Time' to datetime format
    annotations_df['Time'] = pd.to_datetime(annotations_df['Time'], unit='s')  # Adjust unit as necessary    
   
    return annotations_df


# Convert annotations to a regular 4-second time index
def convert_annotations_to_time_index(annotations_df, window_length, file_stem):
    # Extract YYMMDD from the filename stem
    date_str = file_stem[-6:]  # Last 6 characters
    start_date = pd.to_datetime(date_str, format='%y%m%d')
    
    # Adjust annotation times to start from the filename stem date
    annotations_df['Time'] += (start_date - annotations_df['Time'].min())

    # Create a time index with 4-second intervals
    end_date = annotations_df['Time'].max() + pd.Timedelta(seconds=window_length)
    time_index = pd.date_range(start=start_date, end=end_date, freq=f'{window_length}s')

    # Create a DataFrame to hold sleep states for each time point
    sleep_states = pd.DataFrame(index=time_index, columns=['State'])

    # Fill sleep states based on annotations
    for i in range(len(annotations_df)):
        current_time = annotations_df['Time'].iloc[i]
        state = annotations_df['State'].iloc[i]
        
        # Assign the state to all time points until the next annotation time
        if i < len(annotations_df) - 1:
            next_time = annotations_df['Time'].iloc[i + 1]
            mask = (time_index >= current_time) & (time_index < next_time)
            sleep_states.loc[mask, 'State'] = state
        else:
            # For the last state, fill until the end of the time index
            mask = (time_index >= current_time)
            sleep_states.loc[mask, 'State'] = state

    # Forward fill to maintain state across the time intervals
    sleep_states['State'] = sleep_states['State'].ffill()

    return sleep_states


# Load FFT values
def load_fft_values(file_path, start_date):
    fft_df = pd.read_csv(file_path)
    fft_df['Window'] = pd.to_datetime(fft_df['Window'])  # Ensure Time is datetime type

    # Adjust the FFT time index to start from the filename stem date
    min_fft_time = fft_df['Window'].min()
    offset = start_date - min_fft_time
    fft_df['Window'] += offset  # Adjust all FFT times by the calculated offset
    
    # set time to index 
    fft_df.set_index('Window', inplace=True)

    return fft_df



# Main processing
file_stem = annotation_file_path.stem  # Get the filename stem
annotations_df = load_annotations(annotation_file_path)

sleep_states_df = convert_annotations_to_time_index(annotations_df, window_length, file_stem)

# Load FFT values and adjust the time
start_date = pd.to_datetime(file_stem[-6:], format='%y%m%d')  # Extract date from filename stem
fft_df = load_fft_values(fft_file_path, start_date)

# Merge the sleep states and FFT values on time
combined_df = pd.merge_asof(sleep_states_df.reset_index(), fft_df, on='Time', direction='forward')



# read in state annotations in visbrain format 

# read in FFT csv 

# Combine? 

# save output 

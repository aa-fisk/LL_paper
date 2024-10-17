import pdb
import pandas as pd
from pathlib import Path

# Parameters
annotation_dir_path = Path('/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/11_somnotate/02_auto_states/')  
fft_dir_path = annotation_dir_path.parents[1] / '06_fft_files' / '01_script' 
sampling_rate = 256  # Sampling rate in Hz
window_length = 4  # Length of the window in seconds
channels = ['fro', 'occ', 'foc']  # Example channel names

# Load sleep state annotations
def load_annotations(file_path):
    annotations_df = pd.read_csv(
        file_path, delimiter='\t', skiprows=2,
        header=None, names=['State','Time']
    )
    annotations_df['Time'] = pd.to_datetime(
        annotations_df['Time'], unit='s'
    )  # Adjust unit as necessary
    return annotations_df

# Convert annotations to a regular 4-second time index
def convert_annotations_to_time_index(annotations_df, window_length, file_stem):
    date_str = file_stem[-6:]  # Last 6 characters
    start_date = pd.to_datetime(date_str, format='%y%m%d')
    
    # Adjust annotation times to start from the filename stem date
    annotations_df['Time'] += (start_date - annotations_df['Time'].min())

    end_date = annotations_df['Time'].max() + pd.Timedelta(
        seconds=window_length
    )
    time_index = pd.date_range(start=start_date, end=end_date, 
                                freq=f'{window_length}s')

    sleep_states = pd.DataFrame(index=time_index, columns=['State'])

    for i in range(len(annotations_df)):
        current_time = annotations_df['Time'].iloc[i]
        state = annotations_df['State'].iloc[i]
        
        if i < len(annotations_df) - 1:
            next_time = annotations_df['Time'].iloc[i + 1]
            mask = (time_index >= current_time) & (time_index < next_time)
            sleep_states.loc[mask, 'State'] = state
        else:
            mask = (time_index >= current_time)
            sleep_states.loc[mask, 'State'] = state

    sleep_states['State'] = sleep_states['State'].ffill()
    return sleep_states

# Load FFT values
def load_fft_values(file_path, start_date):
    # Read FFT DataFrame with the first two columns as the index
    fft_df = pd.read_csv(file_path, index_col=[0, 1])
    
    # Get the length of the first channel
    num_rows = fft_df.shape[0] // len(channels)

    # Create a new datetime index based on the filename stem
    new_index = pd.date_range(start=start_date, periods=num_rows, freq='4s')

    # Reset index to prepare for combining with new index
    fft_df.reset_index(inplace=True)

    # Create a MultiIndex with the datetime index and channel names
    multi_index = pd.MultiIndex.from_product(
        [new_index, channels], names=['Window', 'Channel']
    )

    # Assign the MultiIndex to the DataFrame
    fft_df = fft_df.loc[:, fft_df.columns[1:]]  # Keep relevant columns
    fft_df.index = multi_index
    
    fft_df.drop(columns=['Window'], inplace=True)    

    return fft_df

# Main processing for multiple files
def process_files(annotation_dir_path, fft_dir_path):
    combined_df = pd.DataFrame()  # Initialize an empty DataFrame

    # Get all annotation files
    annotation_files = list(annotation_dir_path.glob('*.hyp'))

    # Initialize a counter
    total_files = len(annotation_files)
    
    for index, annotation_file in enumerate(annotation_files):

        file_stem = annotation_file.stem
        matching_fft_files = list(
            fft_dir_path.glob(f"{file_stem[:3]}*.csv")
        )
        
        print(f"Processing{file_stem}") 

        if matching_fft_files:
            annotations_df = load_annotations(annotation_file)

            if annotations_df.empty:
                print(f"No annotations found in {annotation_file.name}.")
                continue

            sleep_states_df = convert_annotations_to_time_index(
                annotations_df, window_length, file_stem
            )
            
            # counter of days 
            total_days = len(matching_fft_files)  

            for index_1, fft_file in enumerate(matching_fft_files):
                start_date = pd.to_datetime(file_stem[-6:], 
                                             format='%y%m%d')
                fft_df = load_fft_values(fft_file, start_date)
                
                # Merge the sleep states and FFT values on window
                combined_temp_df = pd.merge_asof(
                    sleep_states_df.reset_index(),
                    fft_df.reset_index(), left_on='index', 
                    right_on='Window', direction='forward'
                )

                # Optionally, include a column for the file source
                combined_temp_df['Source File'] = fft_file.name

                combined_df = pd.concat(
                    [combined_df, combined_temp_df], 
                    ignore_index=True
                )

                # Print progress
                print(f"Processed {index_1 + 1}/{total_days} days.")

        # Print progress
        print(f"Processed {index + 1}/{total_files} files.")

    return combined_df

# Run the processing
final_combined_df = process_files(annotation_dir_path, fft_dir_path)


# save output 
 # Optionally save the combined DataFrame
output_file_path = Path('combined_sleep_states_fft.csv')
#combined_df.to_csv(output_file_path, index=False)
print(f"Saved combined DataFrame to {output_file_path}")

# Output the resulting DataFrame



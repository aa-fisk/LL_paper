import pdb
import pyedflib
import numpy as np
from datetime import timedelta
from pathlib import Path

input_edf_dir = Path(
    "/Users/angusfisk/Documents/01_personal_files/01_work/"
    "11_LL_paper/02_analysis/01_data_files/01_edf/01_script"
)
output_edf_dir = input_edf_dir.parent / "03_test"


def crop_edf_to_24_hours(
        input_edf_path, 
        output_edf_path, 
        file_num, 
        total_files):
    """
    Crop the EDF file to the first 24 hours of data and save it.

    Parameters:
    - input_edf_path (str): The path to the input EDF file.
    - output_edf_path (str): The path to save the cropped EDF file.
    - file_num (int): Current file index (for progress tracking).
    - total_files (int): Total number of files being processed.
    """
    # Open the EDF file for reading
    edf_reader = pyedflib.EdfReader(str(input_edf_path))
    
    # Get the sampling frequency and the duration of the recording
    n_signals = edf_reader.signals_in_file
    sampling_frequencies = edf_reader.getSampleFrequencies()
    
    # Calculate the number of samples corresponding to 24 hours
    # Note: Sampling frequency is in samples per second
    max_samples = int(24 * 60 * 60 * np.min(sampling_frequencies))

    # Get the minimum number of samples for the signals (across all channels)
    total_samples = min(edf_reader.getNSamples()[0], max_samples)

    # Initialize the EDF writer for the output file
    edf_writer = pyedflib.EdfWriter(
        str(output_edf_path), 
        n_channels=n_signals, 
        file_type=pyedflib.FILETYPE_EDFPLUS
    )

    # Set the channel headers from the input file to the output file
    channel_headers = [edf_reader.getSignalHeader(i) for i in range(n_signals)]
    edf_writer.setSignalHeaders(channel_headers)

    # Set the start time of the recording
    edf_writer.setStartdatetime(edf_reader.getStartdatetime())

    # Crop and write data for each signal (channel)
    for signal_index in range(n_signals):
        # Read the signal data from the input EDF file
        signal_data = edf_reader.readSignal(signal_index, start=0, 
                                            n=total_samples)
        
        pdb.set_trace()
        # Write the cropped signal data to the new EDF file
        edf_writer.writePhysicalSamples(signal_data[:total_samples])

    # Close both readers and writers
    edf_reader.close()
    edf_writer.close()

    print(f"Processed file {file_num}/{total_files}: {input_edf_path.name}")

if __name__ == "__main__":
    # List all edf files in input dir 
    file_list = list(input_edf_dir.glob("*.edf"))
    total_files = len(file_list) 
    
    for i, file in enumerate(file_list):
        input_edf_path = file
        output_edf_path = output_edf_dir / str(file.stem + ".edf")

        crop_edf_to_24_hours(input_edf_path, output_edf_path, i, total_files)
        

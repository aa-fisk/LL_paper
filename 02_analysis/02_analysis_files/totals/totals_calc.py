import pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# files and dirs
derivation = "fro"
import_dir = Path(
    "/Users/angusfisk/Documents/01_personal_files/01_work/"
    "11_LL_paper/02_analysis/01_data_files/07_clean_fft_files/01_script"
) / derivation
save_dir = import_dir.parents[3] / "03_analysis_outputs" / "totals"
corrected_dir = import_dir.parents[1] / "02_corrected" / derivation
raw_files = list(import_dir.glob("*.csv"))
corrected_files = list(corrected_dir.glob("*.csv"))

baseline_day = "2018-04-09"


# Define a function to calculate state count per 24 hours
def calculate_state_count(
        data,
        state_col="State",
        state="non-REM",
        start_time="07:00:00"):
    # Resample data to 24-hour periods and calculate state count
    state_mask = data[state_col] == state
    state_count = state_mask.resample("24h", offset=start_time).sum()
    state_seconds = state_count * 4
    return state_seconds


if __name__ == "__main__":

    # Initialize a list to hold the combined counts
    combined_dict = {}

    # Iterate through each file in raw_files and corrected_files
    for raw_file, corrected_file in zip(raw_files, corrected_files):
        # Read in the raw and corrected files
        raw_data = pd.read_csv(
            raw_file, index_col=0, parse_dates=True
        ).sort_index()
        corrected_data = pd.read_csv(
            corrected_file, index_col=0, parse_dates=True
        ).sort_index()

        # Get the list of unique states from the raw data
        state_list = raw_data.iloc[:, 0].unique()

        for curr_state in state_list:
            # Calculate the state counts for both raw and corrected datasets
            raw_state_counts = calculate_state_count(
                raw_data, state=curr_state)
            corrected_state_counts = calculate_state_count(
                corrected_data, state=curr_state)

            # Combine the counts for the current state across raw and corrected
            # files
            combined_counts = pd.concat(
                [raw_state_counts[baseline_day], corrected_state_counts],
            )

            # Add the combined counts to the dictionary
            combined_dict[f"{raw_file.stem}_{curr_state}"] = combined_counts

    # Create a DataFrame with the combined counts
    df_combined_counts = pd.concat(combined_dict, axis=1)

    save_name = save_dir / "total_states.csv"
    df_combined_counts.to_csv(save_name)

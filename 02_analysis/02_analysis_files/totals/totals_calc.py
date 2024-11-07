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


def calculate_state_count(data, state_col="State", state="non-REM",
                          start_time="07:00:00", part="total"):
    """
    Calculate state counts for a given part (total, light, dark).

    Parameters:
    - data: DataFrame containing the time-series data
    - state_col: The column representing the state (default 'State')
    - state: The specific state to calculate counts for (default 'non-REM')
    - start_time: The offset time for 24-hour periods (default '07:00:00')
    - part: 'total', 'light', or 'dark' to specify time range

    Returns:
    - state_seconds: Series of state durations in seconds
    """
    state_mask = data[state_col] == state
    
    if part == "total":
        # Resample data for 24-hour parts
        state_count = state_mask.resample("24h", offset=start_time).sum()
    elif part == "light":
        # First 12 hours (midnight to noon)
        state_count = state_mask.between_time("00:00", "11:59").resample(
            "24h", offset=start_time).sum()
    elif part == "dark":
        # Second 12 hours (noon to midnight)
        state_count = state_mask.between_time("12:00", "23:59").resample(
            "24h", offset=start_time).sum()
    
    # Convert state count to seconds (assuming 4s intervals)
    state_seconds = state_count * 4
    return state_seconds


if __name__ == "__main__":

    # Initialize a list to hold the combined counts
    combined_dict_total = {}
    combined_dict_light = {}
    combined_dict_dark = {}
    dict_list = [combined_dict_total, combined_dict_light, combined_dict_dark] 
    part_list = ["total", "light", "dark"]

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
            # zip through all tipes 
            for curr_dict, curr_part in zip(dict_list, part_list):

                # Calculate the state counts for both raw and corrected datasets
                raw_state_counts = calculate_state_count(
                    raw_data, state=curr_state, part=curr_part)
                corrected_state_counts = calculate_state_count(
                    corrected_data, state=curr_state, part=curr_part)

                # Combine the counts for the current state across raw and corrected
                # files
                combined_counts = pd.concat(
                    [raw_state_counts[baseline_day], corrected_state_counts],
                )

                # Add the combined counts to the dictionary
                curr_dict[f"{raw_file.stem}_{curr_state}"] = combined_counts

    # Create a DataFrame with the combined counts
    for curr_dict, curr_part in zip(dict_list, part_list):
        df_combined_counts = pd.concat(curr_dict, axis=1)

        save_name = save_dir / f"{curr_part}_states.csv"
        df_combined_counts.to_csv(save_name)

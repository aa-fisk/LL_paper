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
corrected_dir = import_dir.parents[1] / "02_corrected" / derivation
raw_files = list(import_dir.glob("*.csv"))
corrected_files = list(corrected_dir.glob("*.csv"))

baseline_day = "2018-04-09"

index_file = 1
raw_file = raw_files[index_file]
corrected_file = corrected_files[index_file]


# Read in the raw and corrected files
raw_data = pd.read_csv(raw_file, index_col=0, parse_dates=True).sort_index()
corrected_data = pd.read_csv(
    corrected_file, index_col=0, parse_dates=True
).sort_index()

# Define a function to calculate NREM count per 24 hours


def calculate_state_count(
        data,
        state_col="State",
        state="non-REM",
        start_time="07:00:00"):
    # Resample data to 24-hour periods and calculate NREM count
    state_mask = data[state_col] == state
    state_count = state_mask.resample("24h", offset=start_time).sum()
    return state_count


# Calculate NREM count per 24 hours for both datasets
raw_nrem_counts = calculate_state_count(raw_data)
corrected_nrem_counts = calculate_state_count(corrected_data)

# combine
combined_counts = pd.concat(
    [raw_nrem_counts[baseline_day], corrected_nrem_counts]
)

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

    # Calculate NREM counts for both datasets
    raw_nrem_counts = calculate_state_count(raw_data)
    corrected_nrem_counts = calculate_state_count(corrected_data)

    combined_counts = pd.concat(
        [raw_nrem_counts[baseline_day], corrected_nrem_counts]
    )

    combined_dict[raw_file.stem] = combined_counts

# Create a DataFrame with the combined counts as a single column
df_combined_counts = pd.DataFrame.from_dict(combined_dict)


# Plot the NREM counts
plt.figure(figsize=(10, 6))
plt.plot(combined_counts)
plt.xlabel('Date')
plt.ylabel('NREM Count per 24 hours')
plt.title('NREM Count per 24 Hours for Raw and Corrected Data')
plt.show()

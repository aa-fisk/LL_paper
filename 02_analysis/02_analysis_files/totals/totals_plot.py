import pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
sns.set()

# files and dirs
import_dir = Path(
    "/Users/angusfisk/Documents/01_personal_files/01_work/"
    "11_LL_paper/02_analysis/03_analysis_outputs/totals/"
)
file = list(import_dir.glob("*csv"))[0]
states = ["awake", "non-REM", "REM"]

# read in the data in hours
data = pd.read_csv(file, index_col=0, parse_dates=True) / 60**2
data.columns = data.columns.str.strip() # remove whitespaces

for curr_state in states:
    # remove last day of data
    data_minus = data.iloc[:-1]
    # use regex pattern to capture just the curr state
    regex_pattern = fr"_(?<!non-)({curr_state})$"
    data_state = data_minus.filter(regex=(regex_pattern))
    print(data_state.tail())

    # Plot individual lines with 0.5 opacity
    fig, ax = plt.subplots(figsize=(15,10))
    ax.plot(data_state.index.date, data_state.values, color='grey', alpha=0.5)

    # Calculate the mean and SEM (Standard Error of the Mean)
    mean = data_state.mean(axis=1)
    sem = data_state.sem(axis=1)

    # Plot the mean as a bold line
    ax.plot(
        data_state.index.date,
        mean,
        color='blue',
        linewidth=2,
        label='Mean')

    # Plot the shaded area for the SEM
    ax.fill_between(
        data_state.index.date,
        mean - sem,
        mean + sem,
        color='blue',
        alpha=0.3,
        label='Mean ± SEM')

    # Set axis labels
    ax.set_xlabel("Date")
    ax.set_ylabel(f"{curr_state.capitalize()} duration")
    ax.set_title(f"{curr_state.capitalize()} State Data Over Time")

    # Format x-axis to show only the date (no time)
    ax.xaxis.set_major_formatter(
        plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))

    # Rotate the date labels for better readability
    plt.xticks(rotation=45)

    # Add a legend
    ax.legend()

    # Show the plot
    plt.tight_layout()
    #plt.show()
    
    # Save the plot 
    fig.set_size_inches(15, 10)
    save_name = import_dir / f"{curr_state}.png"
    fig.savefig(save_name)


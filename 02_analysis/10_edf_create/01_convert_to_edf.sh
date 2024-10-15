#!/bin/bash



ascii="/Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/ascii2edf/ascii2edf"

# apply ascii function 
#$asciif $first_file $template_file "Mouse" "date" "2018" "04" "09" "00" "00" "00" save_name

# Directory containing the input files
input_directory="/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/02_txt"

# Directory to store the output EDF files
output_directory="/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/01_edf/01_script"

# Create output directory if it doesn't exist
mkdir -p "$output_directory"

# Loop through each file in the input directory
for file in "$input_directory"/*; do
    # Check if it's a file
    if [[ -f "$file" ]]; then
        # Get the base name of the file (without the directory path)
        base_name=$(basename "$file")
        echo $base_name
        
        # Run ascii2edf on the file
        # Change `ascii2edf` to the full path if necessary
        $ascii "$file" $template_file "Mouse" "date" "2018" "04" "09" "00" "00" "00" "$output_directory/${base_name%.txt}.edf"  # Adjust file extension as needed

        # Check if the command succeeded
        if [[ $? -eq 0 ]]; then
            echo "Converted $file to $output_directory/${base_name%.txt}.edf"
        else
            echo "Failed to convert $file"
        fi
    fi
done


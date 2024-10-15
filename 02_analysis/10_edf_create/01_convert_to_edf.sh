#!/bin/bash



ascii="/Users/angusfisk/Documents/01_personal_files/01_work/09_github_repos/ascii2edf/ascii2edf.c"

echo "hello world"

# get template file 
template_file=$(find "$PWD"/*.xml -maxdepth 1 -type f | head -n 1)
echo $template_file

# get list of files to iterate through
file_dir="/Users/angusfisk/Documents/01_personal_files/01_work/11_LL_paper/02_analysis/01_data_files/02_txt"

# use just first file debug
first_file=$(find "$file_dir" -maxdepth 1 -type f | head -n 1)
echo ${first_file}

# create save file name
save_name="${first_file%/*}/test_edf.edf"
echo $save_name

# apply ascii function 
$asciif $first_file $template_file "Mouse" "date" "2018" "04" "09" "00" "00" "00" save_name

# Good!
#for f in "$file_dir"/*; do
#    echo "$f"
#
#done 
#!/bin/bash

# Directory containing the input files
input_directory="/path/to/your/directory"

# Directory to store the output EDF files
output_directory="/path/to/output/directory"

# Create output directory if it doesn't exist
mkdir -p "$output_directory"

# Loop through each file in the input directory
for file in "$input_directory"/*; do
    # Check if it's a file
    if [[ -f "$file" ]]; then
        # Get the base name of the file (without the directory path)
        base_name=$(basename "$file")
        
        # Run ascii2edf on the file
        # Change `ascii2edf` to the full path if necessary
        ascii2edf "$file" -o "$output_directory/${base_name%.txt}.edf"  # Adjust file extension as needed

        # Check if the command succeeded
        if [[ $? -eq 0 ]]; then
            echo "Converted $file to $output_directory/${base_name%.txt}.edf"
        else
            echo "Failed to convert $file"
        fi
    fi
done


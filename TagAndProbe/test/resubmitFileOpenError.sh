#!/bin/bash

# Check if an argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <path_to_directory>"
    exit 1
fi

target_dir=$1

# Check if the directory exists
if [ ! -d "$target_dir" ]; then
    echo "Error: Directory $target_dir does not exist."
    exit 1
fi

# Loop through subdirectories
for dir in "$target_dir"
do
    cd "$dir" || continue  # Avoid errors if cd fails
    user=$(pwd | cut -d"/" -f4)

    # Loop through log files
    for logfile in log*.txt
    do
        tmp=${logfile#*_}
        idx=${tmp%.*}
        out=$(grep -r "FileOpenError" "$logfile")
        
        if [[ $out == "An exception of category 'FallbackFileOpenError' occurred while" ]]; then
            echo "Resubmitting job num $idx"
            /home/llr/cms/$user/t3submit -short "job_$idx.sh"
        fi
    done
    cd - > /dev/null  # Return to the previous directory, suppress output
done

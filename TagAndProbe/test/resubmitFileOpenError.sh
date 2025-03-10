#!/bin/bash

# sh resubmitFileOpenError.sh folder_to_scan 

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

    for logfile in log*.txt
    do
        tmp=${logfile#*_}
        idx=${tmp%.*}
        
        # Check for FileOpenError
        if grep -q "An exception of category 'FallbackFileOpenError' occurred while" "$logfile"; then
            echo "Resubmitting job num $idx with -short due to FileOpenError"
            /home/llr/cms/$user/t3submit -short "job_$idx.sh"
            continue  # No need to check further, since we already resubmitted
        fi

        # Check for fatal system signal
        if grep -q "A fatal system signal has occurred: abort signal" "$logfile"; then
            echo "Resubmitting job num $idx with -short due to fatal system signal"
            /home/llr/cms/$user/t3submit -short "job_$idx.sh"
            continue  # No need to check further, since we already resubmitted
        fi

        # Check for fatal system signal
        if grep -q "End Fatal Exception" "$logfile"; then
            echo "Resubmitting job num $idx with -short due to End Fatal Exception"
            /home/llr/cms/$user/t3submit -short "job_$idx.sh"
            continue  # No need to check further, since we already resubmitted
        fi
        
        # Check if TrigReport is missing
        if ! grep -q "TrigReport ---------- Event  Summary ------------" "$logfile"; then
            echo "Resubmitting job num $idx with -long due to missing TrigReport"
            /home/llr/cms/$user/t3submit -long "job_$idx.sh"
        fi
    done
    cd - > /dev/null  # Return to the previous directory, suppress output
done

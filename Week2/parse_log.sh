#!/bin/bash

# Step 1: User enters the path to the log file
read -p "Enter the path to the log file: " log_file

# Step 2: User enters the path to the output file
read -p "Enter the path to the output file: " output_file

# Step 3: User enters the pattern to search for in the log file
read -p "Enter the pattern to search for in the log file: " search_pattern

# Step 4: Script parses the log file for the search pattern and forwards the result to the output file
if [ -f "$log_file" ]; then
    if [ ! -f "$output_file" ]; then
        touch "$output_file"
    fi

    while read -r line; do
    if [[ $line == *"$search_pattern"* ]]; then
        timestamp=$(echo "$line" | awk '{print $1, $2}')
        value=$(echo "$line" | awk -F "$search_pattern" '{print $2}')
        echo "$timestamp $value" >> $output_file
    fi
done < "$log_file"
    echo "Search results have been forwarded to '$output_file'."
else
    echo "Error: The log file '$log_file' does not exist."
fi

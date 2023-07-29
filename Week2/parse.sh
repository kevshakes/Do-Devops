#!/bin/bash

# Step 1: User enters the path to the log file
read -p "Enter the path to the log file: " log_file

# Step 2: User enters the path to the output file
read -p "Enter the path to the output file: " output_file

# Step 3: User enters the pattern to search for in the log file
read -p "Enter the pattern to search for in the log file: " search_pattern

# Step 4: Use awk to parse the log file for the search pattern and save the result to the output file
awk "/$search_pattern/" "$log_file" > "$output_file"

echo "Parsing complete."

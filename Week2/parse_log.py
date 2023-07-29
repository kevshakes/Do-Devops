import subprocess

def parse_log(log_file, output_file, search_pattern):
    # Use awk to parse the log file for the search pattern and save the result to the output file
    awk_command = f"awk '/{search_pattern}/' {log_file} > {output_file}"
    subprocess.run(awk_command, shell=True)

if __name__ == "__main__":
    # Get input from the user
    log_file = input("Enter the path to the log file: ")
    output_file = input("Enter the path to the output file: ")
    search_pattern = input("Enter the pattern to search for in the log file: ")

    # Call the function to parse the log file
    parse_log(log_file, output_file, search_pattern)

    print("Parsing complete.")

import re

def find_ip_addresses(text):
    # Regular expression pattern for matching IP addresses
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    # Find all occurrences of IP addresses in the text
    ip_addresses = re.findall(ip_pattern, text)

    return ip_addresses

if __name__ == "__main__":
    # Get text input from the user
    user_input = input("Enter the text to search for IP addresses:\n")

    # Find IP addresses in the user-provided text
    ip_addresses_found = find_ip_addresses(user_input)

    # Print the results
    if ip_addresses_found:
        print("IP addresses found:")
        for ip_address in ip_addresses_found:
            print(ip_address)
    else:
        print("No IP addresses found in the text.")

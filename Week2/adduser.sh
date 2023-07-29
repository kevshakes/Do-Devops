#!/bin/bash

# Script to create a new user account on a Linux system using adduser

# Step 1: Adding the desired username
read -p "Enter the desired username: " username

# Step 2: Checking if the user exists
if id "$username" &>/dev/null; then
  echo "User '$username' already exists."
else
  # Step 3: If the user name does not exist, it will be added
  sudo adduser "$username"

  # Step 4: Showing User ID, Group ID, and Group
  user_id=$(id -u "$username")
  group_id=$(id -g "$username")
  group_name=$(id -gn "$username")

  echo "User '$username' has been created."
  echo "User ID: $user_id"
  echo "Group ID: $group_id"
  echo "Group: $group_name"
fi

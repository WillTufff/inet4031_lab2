#!/bin/bash

# Declare an array of strings
user_array=("user1" "user2" "user3")

# Iterate over the elements of the array and print each one
for user in "${user_array[@]}"
do
  echo "$user"
done

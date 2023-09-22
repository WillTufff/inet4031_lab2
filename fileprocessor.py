#!/usr/bin/env python3
with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()

print("Printing out User Data:\n")

for line in lines:

	fields = line.strip().split(':')

	if not fields[0].startswith('#'):
		username = fields[0]
		password = fields[1]
		userid = fields[2]
		groupid = fields[3]

		print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
	else:
		username = fields[0]
		username = username[1:]
		print(f"{username} is skipped because it starts with a hashtag (is commented out)")

print("\nend of user data")

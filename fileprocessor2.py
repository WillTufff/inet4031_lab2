#!/usr/bin/env python3

import sys

print("Printing out User Data:\n")

for line in sys.stdin:
	line = line.strip()

	if not line:
		continue

	fields = line.split(':')

	if len(fields) >= 4:
		username = fields[0]
		password = fields[1]
		userid = fields[2]
		groupid = fields[3]

		print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
	else:
		print(f"Skipping line: {line} (Invalid format)")

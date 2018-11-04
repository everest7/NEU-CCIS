import csv
import re


with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skip first line
    for line in csv_reader:
        pattern = re.compile(r'@[a-zA-Z0-9-._]+\.(\w+)')
        matches = pattern.search(line[3])
        print(matches.group(1))

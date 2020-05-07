import csv

with open('/Users/nima/github/python-level-2/Examples/data/input.csv', 'r') as file:
    reader = csv.DictReader(file)

    for person in reader:
        print(f'{person["Name"]} is {person["Age"]}')

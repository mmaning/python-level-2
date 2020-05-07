"""
Read a file with a number on each line. Print the sum of those numbers.
"""

sum = 0
with open('/Users/nima/github/python-level-2/Examples/data/input.txt', 'r') as file:
    for line in file.readlines():
        num = int(line)
        sum += num

print(f'Sum is {sum}')

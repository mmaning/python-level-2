"""
A program that takes a letter and outputs a text file of
all of the countries that start with that letter
"""

# Todo: Read data/countries.txt and save all countries in a dictionary key:first_letter, value:country_name
country_dict = {}

with open('/Users/nima/github/python-level-2/Problems/data/countries.txt', 'r') as file:
    for line in file.readlines():
        country_name = line.strip()
        first_letter = country_name[0].upper()
        if first_letter not in country_dict:
            country_dict[first_letter] = []   # add the first_letter to the dictionary with Null value
        country_dict[first_letter].append(country_name)

print(country_dict)


# Get user to provide a letter
letter = input('Number of countries that start with letter: ')

# Todo: Print the number of countries that start with the letter

letter = letter.capitalize()

num_countries = len(country_dict.get(letter, []))
print(country_dict[letter])
print(num_countries)

# Todo: Create text file that lists the countries starting with the letter

with open(f'/Users/nima/github/python-level-2/Problems/data/{letter}_country_list.txt', 'w') as output_file:
    output_file.write(str(country_dict[letter]))


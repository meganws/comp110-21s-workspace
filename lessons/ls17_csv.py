"""Example reading CSV files."""

from csv import DictReader

# utf8 allows us to have more character sets (emojis, arabic, etc)
file_handle = open('data/weather.csv', 'r', encoding='utf8')
csv_reader = DictReader(file_handle)

# a "table" can be modeled as a list of rows, where a row
# is a dictionary with a column title as the key
table: list[dict[str, str]] = []

# add each row of data to our table
for row in csv_reader:
    table.append(row)

# when we're done reading / working with a file, we should close it!
file_handle.close()

# calculate the average high temp
# process the table by a specific column
high_temps: list[float] = []
for row in table:
    high_temps.append(float(row['high']))
print(high_temps)

print('The average high temp was: ')
avg_high: float = sum(high_temps) / len(high_temps)
print(avg_high)
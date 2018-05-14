import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # call next() one time to get the first line of the file
    header_row = next(reader)
    # print(header_row)

    # to make it  easier to understand the file header data
    # print each header and pos in list
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

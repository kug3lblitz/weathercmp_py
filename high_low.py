import csv
from matplotlib import pyplot as plt
from datetime import datetime

# get dates and high temps from file, convert from strs to ints to visualize
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # to find high temp data in file, we print each header and its position
    # for index, column_header in enumerate(header_row):
        # print(index, column_header)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

    # plot data
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')

    # format plot
    plt.title("Daily high temperatures, July 2014, Sitka, AK", fontsize=24)
    plt.xlabel('', fontsize=16)
    # draw xlabels diagonally to prevent overlap
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# by sam crawford, the scope of this program is to pull data from a .csv file, weather temperatures in sitka, ak for the year 2014, then to create an x,y graph of highs, and lows, while shading the area between.
# the graph is labeled with temp on y, and date on y for the entire year of 2014. Also this is the first real pythong app I have written since completeing a course on python.
import csv  #imports CSV module 
from datetime import datetime

from matplotlib import pyplot as plt #imports plotting tools.

#get dates, high and low temperatures from file
filename = 'sitka_weather_2014.csv'
with open(filename) as f:    #Python opens up the file, then uses the csv module to extract data.
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []  #From the various pieces of data, I chose date, High Temps, and Low Temps. I left the lists empty.
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d") #The date-time module is used to convert the numerical date in the csv file, into a string stating the date.
        dates.append(current_date)

        high = int(row[1]) # here I defined the variable high as an integer or Row 1 
        highs.append(high) #then appended highs to high

        low = int(row[3]) # same as with the highs.
        lows.append(low)

#plot data
fig = plt.figure(dpi=128, figsize=(10, 6)) # i defined a fiure to be plotted using the matplotlib module, then defined the high temps day/temp to plot, and be red.
plt.plot(dates, highs, c='red', alpha=0.5) # and the lows to be blues, then to fill in the space between the High Temp line and low temp line.
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot-graph giving a title, labeling the x and y axis' fontsize and plot the data from the file, creating a cool x,y graph.
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
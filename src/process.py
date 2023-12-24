import csv

with open('../data/logs.csv', 'r') as f:
    reader = csv.reader(f)
    logs = list(reader)

print(logs[1])

# Extract dates and times
dates_and_times = [[log[3], log[4]] for log in logs[1:]]
num_dates = len(dates_and_times)

# Convert 'MM/DD/YY' to 'YY-MM-DD' using datetime.strptime
from datetime import datetime
dates_and_times = [[datetime.strptime(date, '%m/%d/%y').strftime('%y-%m-%d'), time] for date, time in dates_and_times]
dates_and_times = sorted(dates_and_times, key=lambda x: x[0])
#for date, time in dates_and_times:
#    print(date, time)

num_dates = len(set([date for date, time in dates_and_times]))

# Count how many of each date and collect count for average
collection = 0
from collections import Counter
for date, count in Counter([date for date, time in dates_and_times]).items():
    collection += count
average = collection / (num_dates)
#print(average)

# Plot the number of logs per day
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.bar([date for date, count in Counter([date for date, time in dates_and_times]).items()], [count for date, count in Counter([date for date, time in dates_and_times]).items()])
# Make the x-axis labels easier to read
plt.xticks(rotation=45)

# Plot average
plt.axhline(y=average, color='r', linestyle='-')

# Label axes
plt.ylabel('Objects logged')
plt.xlabel('Date')

#plt.show()

# ~30 trips, ~3 entries per trip

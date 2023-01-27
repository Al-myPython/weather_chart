import csv
from matplotlib import pyplot as plt
from datetime import datetime

f = open('data/bude_cornwall_uk_2021_weather.csv')
reader = csv.reader(f)
header_column = next(reader)


# Plot highs and lows temperatures for Bude, Cornwall, UK for 2021 (Metric system)
dates, highs, lows = [], [], []
for column in reader:
    current_date = datetime.strptime(column[2], '%Y-%m')
    try:
        high = float(column[6])
        low = float(column[7])
    except ValueError:
        print(f"Missing date: {current_date}.")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

   # Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
ax.set_title("Monthly High and Low Temperatures for Bude, Cornwall, UK", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperatures (Celsius)", fontsize=16)

plt.show()





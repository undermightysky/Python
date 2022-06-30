# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

# time, temperature (deg C), humidity (%), air quality (ppb)

# read the CSV file and configure everything right now
df = pd.read_csv('Sensor_0204.csv',
                 delimiter='$',
                 names=['Time', 'Temperature', 'Humidity', 'Air Quality'],
                 index_col='Time',
                 parse_dates=['Time'],
                 )

print(df)

# or read the CSV file first and then configure the DataFrame
# df = pd.read_csv('Sensor_0204.csv', delimiter='$')
# df.columns = ['Time', 'Temperature', 'Humidity', 'Air Quality']
# df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S.%f')
# df.set_index('Time', inplace=True)

# plot the entire DataFrame
df.plot(subplots=True, grid=True)
plt.tight_layout()
plt.savefig('sensordaten.pdf')


# calculate the average values
df_mean = pd.DataFrame()
for start, end in zip(pd.date_range("2020-01-01", periods=24, freq="MS"),
                      pd.date_range("2020-02-01", periods=24, freq="MS")):

    # compute the average over the current time span
    m = df[start:end].mean()
    # insert a new column
    m['Time'] = start
    # append the Series to the DataFrame
    df_mean = df_mean.append(m, ignore_index=True)


# define the 'Time' column as the index
df_mean.set_index('Time', inplace=True)

print(df_mean)

# plot the averaged data
df_mean.plot(subplots=True, grid=True, style='.-')
plt.tight_layout()
plt.savefig('sensordaten_mittelwert.pdf')

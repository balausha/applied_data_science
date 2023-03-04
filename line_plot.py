import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matches = pd.read_csv('matches.csv')
#creating new column for Year by extracting Year from date column
matches["Year"] = year=pd.DatetimeIndex(matches['date']).year


csk = matches[matches["winner"] == "Chennai Super Kings"]
rcb = matches[matches["winner"] == "Royal Challengers Bangalore"]
mi = matches[matches["winner"] == "Mumbai Indians"]
sh = matches[matches["winner"] == "Sunrisers Hyderabad"]
kkr = matches[matches["winner"] == "Kolkata Knight Riders"]

plt.figure(figsize=(12, 6))
plt.plot(mi['Year'].value_counts().sort_index(), label="Mumbai Indians")
plt.plot(sh['Year'].value_counts().sort_index(), label="Sunrisers Hyderabad")
plt.plot(kkr['Year'].value_counts().sort_index(), label="Kolkata Knight Riders")

plt.title("Number of matches won by three IPL teams")
plt.xlabel("Number of time a team won")
plt.ylabel("Year")
plt.xticks(np.arange(2008, 2019, 1))
plt.legend()
plt.show()

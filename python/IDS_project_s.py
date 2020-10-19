# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:21:51 2020

@author: sampp
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("datapos.csv")

flights = data[["DAY_OF_MONTH","DAY_OF_WEEK", "OP_UNIQUE_CARRIER","ORIGIN","DEST","DEP_DELAY","DEP_DELAY_NEW","DEP_DEL15","ARR_DELAY","ARR_DEL15",
               "CANCELLED","CANCELLATION_CODE","DISTANCE","CARRIER_DELAY", "WEATHER_DELAY", "NAS_DELAY", "SECURITY_DELAY", "LATE_AIRCRAFT_DELAY"]]

for flight in flights:
    flights.loc[flights['CARRIER_DELAY'] >0, 'DELAY_CODE'] = 1
    flights.loc[flights['WEATHER_DELAY'] >0, 'DELAY_CODE'] = 2
    flights.loc[flights['NAS_DELAY'] >0, 'DELAY_CODE'] = 3
    flights.loc[flights['SECURITY_DELAY'] >0, 'DELAY_CODE'] = 4
    flights.loc[flights['LATE_AIRCRAFT_DELAY'] >0, 'DELAY_CODE'] = 5
    
    
day_delay = flights[['DAY_OF_MONTH', 'DEP_DELAY_NEW']]
day_delay = day_delay.groupby(by='DAY_OF_MONTH').sum()
day_delay=day_delay.reset_index(drop=False)

###
#minutes wasted

plt.figure(1)
sns.barplot(x="DAY_OF_MONTH", y=day_delay["DEP_DELAY_NEW"]/60, data=day_delay)
plt.title("Hours wasted by delayed flights")
plt.ylabel("Sum of delayed minutes")
plt.xlabel("Day of Month")
plt.show()

###
#Cancelled / Delayed

flights_del = flights.loc[flights['DEP_DELAY_NEW'] >0]
flights_canc =  flights.loc[flights['CANCELLED'] == 1]

flights_all_count = flights.groupby("DAY_OF_MONTH").count()
flights_del_count = flights_del.groupby("DAY_OF_MONTH").count()
flights_canc_count = flights_canc.groupby("DAY_OF_MONTH").count()

plt.figure(2)

plt.plot(flights_all_count["DEST"], label = "All flights")
plt.plot(flights_del_count["DEST"], label = "Delayed flights")
plt.plot(flights_canc_count["DEST"], label = "Cancelled flights")

plt.title("Delayed flights and Cancelled flights")
plt.ylabel("Number of flights")
plt.xlabel("Day of month")
plt.legend(loc='best', bbox_to_anchor=(0.5, 0., 0.5,0.5))
plt.show

####

#Delay reasons

plt.figure(3)
sns.countplot('DELAY_CODE', data=flights)
plt.title("Delay reasons")
plt.xlabel("Delay Reason")
plt.ylabel("Number of flights")
plt.legend()
plt.show()

###
#Delay carriers


delayed_flights = flights.loc[flights["DEP_DELAY_NEW"] > 0]

plt.figure(4)
sns.barplot('OP_UNIQUE_CARRIER','CARRIER_DELAY', data=delayed_flights)

plt.title("Delays caused by Carrier")
plt.xlabel("Unique Carriers")
plt.ylabel("Average Delay in Minutes")
plt.show()



###
#worst days

week_count = flights.groupby("DAY_OF_WEEK").count()
week_del_count = flights_del.groupby("DAY_OF_WEEK").count()

plt.figure(5)
plt.plot(week_count["DEST"])
plt.plot(week_del_count["DEST"])
plt.title("Delayed flights by weekday")
plt.xlabel("Day of week")
plt.ylabel("Number of flights")
plt.show()


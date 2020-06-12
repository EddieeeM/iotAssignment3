# Importing Libraries
import pandas as pd
from pandas import read_csv
from matplotlib import pyplot as plt

# Load dataset
url = "https://soundlightdata.s3-ap-southeast-2.amazonaws.com/Data.csv"
names = ['id','temperature','lumens','location','date', 'time']
dataset = read_csv(url, names = names)

# Mean, STDev, Variance --> Location1
print("Location 1 Data")
print('%s: Mean: %f, StDev: %f, Variance: %f' % ('Lumens -->', dataset.query('location == "location1"')['lumens'].mean(), dataset.query('location == "location1"')['lumens'].std(), dataset.query('location == "location1"')['lumens'].var()))
print('%s: Mean: %f, StDev: %f, Variance: %f \n' % ('Temperature -->', dataset.query('location == "location1"')['temperature'].mean(), dataset.query('location == "location1"')['temperature'].std(), dataset.query('location == "location1"')['temperature'].var()))

# Mean, STDev, Variance --> Location2
print("Location 2 Data")
print('%s: Mean: %f, StDev: %f, Variance: %f' % ('Lumens -->', dataset.query('location == "location2"')['lumens'].mean(), dataset.query('location == "location2"')['lumens'].std(), dataset.query('location == "location2"')['lumens'].var()))
print('%s: Mean: %f, StDev: %f, Variance: %f \n' % ('Temperature -->', dataset.query('location == "location2"')['temperature'].mean(), dataset.query('location == "location2"')['temperature'].std(), dataset.query('location == "location2"')['temperature'].var()))

# Mean, STDev, Variance --> Location3
print("Location 3 Data")
print('%s: Mean: %f, StDev: %f, Variance: %f' % ('Lumens -->', dataset.query('location == "location3"')['lumens'].mean(), dataset.query('location == "location3"')['lumens'].std(), dataset.query('location == "location3"')['lumens'].var()))
print('%s: Mean: %f, StDev: %f, Variance: %f \n' % ('Temperature -->', dataset.query('location == "location3"')['temperature'].mean(), dataset.query('location == "location3"')['temperature'].std(), dataset.query('location == "location3"')['temperature'].var()))

# Stores Lumens 
Location1_Lumens = []
Location2_Lumens = []
Location3_Lumens = []
Location1_Lumens.append(dataset.query('location == "location1"')['lumens'])
Location2_Lumens.append(dataset.query('location == "location2"')['lumens'])
Location3_Lumens.append(dataset.query('location == "location3"')['lumens'])

# Stores Temperature
Location1_Temp = []
Location2_Temp = []
Location3_Temp = []
Location1_Temp.append(dataset.query('location == "location1"')['temperature'])
Location2_Temp.append(dataset.query('location == "location2"')['temperature'])
Location3_Temp.append(dataset.query('location == "location3"')['temperature'])


# Normal Plots
fig, axes1 = plt.subplots(2,2)
axes1[0,0].set_title("Temperature (Overall)")
axes1[0,0].set_xlabel("Id's")
axes1[0,0].set_ylabel("Temperature (°c) ")
axes1[0,0].plot(dataset.id, dataset.temperature, label = 'Temperature')
axes1[0,1].set_title("Lumens (Overall)")
axes1[1,0].set_xlabel("Id's")
axes1[1,0].set_ylabel("Lumens (lm)")
axes1[0,1].plot(dataset.id, dataset.lumens, label = 'Lumens')
axes1[1,0].set_title("Temperature Graph")
axes1[1,0].set_xlabel("Lumens (lm)")
axes1[1,0].set_ylabel("Temperature (°c) ")
axes1[1,0].plot(dataset.lumens, dataset.temperature, label = 'Temp/Light')
axes1[1,1].set_title("Lumens Graph")
axes1[1,1].set_xlabel("Temperature (°c)")
axes1[1,1].set_ylabel("Lumens (lm)")
axes1[1,1].plot(dataset.temperature, dataset.lumens, label = 'Light/Temp')

# Location Lumens
fig2, axes2 = plt.subplots(2,2)
axes2[0,0].set_title("Location1 Lumens")
axes2[0,0].set_xlabel("Location 1")
axes2[0,0].set_ylabel("Lumens (lm)")
axes2[0,0].boxplot(Location1_Lumens)
axes2[0,1].set_title("Location2 Lumens")
axes2[0,1].set_xlabel("Location 2")
axes2[0,1].set_ylabel("Lumens (lm)")
axes2[0,1].boxplot(Location2_Lumens)
axes2[1,0].set_title("Location3 Lumens")
axes2[1,0].set_xlabel("Location 3")
axes2[1,0].set_ylabel("Lumens (lm)")
axes2[1,0].boxplot(Location3_Lumens)

# Location Temps
fig3, axes3 = plt.subplots(2,2)
axes3[0,0].set_title("Location1 Temp")
axes3[0,0].set_xlabel("Location 1")
axes3[0,0].set_ylabel("")
axes3[0,0].boxplot(Location1_Temp)
axes3[0,1].set_title("Location2 Temp")
axes3[0,1].set_xlabel("Location 2")
axes3[0,1].set_ylabel("")
axes3[0,1].boxplot(Location2_Temp)
axes3[1,0].set_title("Location3 Temp")
axes3[1,0].set_xlabel("Location 3")
axes3[1,0].set_ylabel("Temperature")
axes3[1,0].boxplot(Location3_Temp)

# Adjusting Plots
fig.subplots_adjust(hspace = 0.6, wspace = 0.6)
fig2.subplots_adjust(hspace = 0.6, wspace = 0.6)
fig3.subplots_adjust(hspace = 0.6, wspace = 0.6)
plt.show()
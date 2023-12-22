#!/usr/bin/env python
# coding: utf-8

# # Weather Dataset import

# In[ ]:


import pandas as pd


# In[ ]:


data=pd.read_csv("C:\\Users\\User\\Downloads\\file.csv")


# In[ ]:


data


# # Data Exploration

# In[ ]:


data.head()


# In[ ]:


data.shape


# In[ ]:


data.index


# In[ ]:


data.columns


# In[ ]:


data.dtypes


# In[ ]:


data["Weather"].unique()


# In[ ]:


data.nunique()


# In[ ]:


data.count()     #for counting non-null values


# In[ ]:


data["Weather"].value_counts()


# In[ ]:


data.info()


# # 1.  Find all the unique "Wind Speed" values in the data

# In[ ]:


data["Wind Speed_km/h"].nunique()


# In[ ]:


data["Wind Speed_km/h"].unique()


# # 2. Find the number of times when the weather is exactly "Clear"

# In[ ]:


data["Weather"].value_counts()

## Answer is 1326


# In[ ]:


## Filtering

data[data.Weather=="Clear"]

#Answer is 1326


# In[ ]:


## group by

data.groupby("Weather").get_group("Clear")

## Answer is 1326


# # 3. Find the number of times when the wind speed was exactly 4km/h

# In[ ]:


data.head(2)


# In[ ]:


data[data["Wind Speed_km/h"]==4]

## Answe is 474


# # 4. How many null values are there in the dataset?

# In[ ]:


data.isnull().sum()

##Answer is 0


# # 5. Rename the name of "Weather" to "Weather Conditions"

# In[ ]:


data.rename(columns = {"Weather":"Weather Conditions"},inplace=True)


# In[ ]:


data.head()


# # 6. What is the mean "Visibility"?

# In[ ]:


data["Visibility_km"].mean()

#mean visibility is 27.66


# # 7. What is the Standard Deviation of "Pressure" in this data?

# In[ ]:


import numpy as np


# In[ ]:


std_deviation=np.std(data.Press_kPa)
print(std_deviation)


# In[ ]:


## Standard deviation of pressure 0.843


# # 8. What is the variance of relative humidity?

# In[ ]:


data.head()


# In[ ]:


var_relhum=np.var(data["Rel Hum_%"])
print(var_relhum)


# In[ ]:


## Variance of Relative Humidity is 286.21


# # 9. Find all instances where "snow" was recorded.

# In[ ]:


data[data["Weather Conditions"]=="Snow"]


# In[ ]:


## There are 390 instances of "Snow" and all the instances are shown above


# # 10. Find all instances when "Wind Speed" is above 24 and "Visibility" is 25.

# In[ ]:


data.head(2)


# In[ ]:


data[(data["Wind Speed_km/h"]>24) & (data["Visibility_km"]==25)]


# In[ ]:


##There are total of 308 instances of the above mentioned type


# # 11. What is the Mean value of each column against each "Weather Condition"

# In[ ]:


data.groupby("Weather Conditions").mean()


# In[ ]:


##The answers are shown in the above table


# # 12. What is the minimum and maximum value of each column against each "weather Condition"?

# In[ ]:


data.groupby("Weather Conditions").agg(["min","max"])


# # 13. Show all the records where "Weather Condition" is Fog.

# In[ ]:


data[data["Weather Conditions"]=="Fog"]


# In[ ]:


##There are total of 150 instances of fog


# # 14. Find all instances when "Weather Conditions" is clear or "Visibility" is above 40.

# In[ ]:


data[(data["Weather Conditions"]=="Clear") | (data["Visibility_km"]>40)]


# In[ ]:


##There are total of 3027 instances of this kind.


# # Correlation Plots

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


# # 1. Correlation Heat Map

# In[ ]:


corr_matrix = data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)


# In[ ]:


#### Insight-1 #########
# As the correlation coefficient between "temperature" and "dew point temperature" is very close to 1, it can be said that
# as one Increases the other one also tends to increase


# In[ ]:


#### Insight-2 ######
# It can be seen that a correlation coefficient of -0.63 exists between "Relative Humidity" and "Visibility"
#So it can be said that as one increases another tends to decrease


# In[ ]:


#### Insight-3 #####
# There exists a correlation coefficient of 0.0049 between "wind speed" and "visibility" which is very close to 0 
# So it maybe said that "Wind Speed" and "Visibility" are almost independent factors.


# # 2. Count Plot of Weather Conditions

# In[ ]:


sns.countplot(x='Weather Conditions', data=data)
plt.xticks(rotation=90)


# In[ ]:


#### Insight -1 #####
#The plot suggests that in the region most of the year the weather condition is clear


# In[ ]:


##### Insight -2 #####
# If the weather condition is not clear, most likely weather condition is cloudy, it doesn't rain that much in the area


# In[ ]:


#### Insight -3#####
#Thunderstroms don't happen very often in the region


# In[ ]:


#### Insight -4 ####
# Weather condition might be foggy at times with some sort of drizzle


# In[ ]:





# In[ ]:


sns.pairplot(data[['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%', 'Wind Speed_km/h', 'Visibility_km', 'Press_kPa']], diag_kind='kde')


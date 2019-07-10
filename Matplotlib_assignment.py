# Generate three arrays of 500 values,  x ,  y1 ,  y2  such that {x∣−2π≤x≤2π}
# y1=sin(x)
# y2=cos(x)
 
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

y1 = np.sin(x)

y2 = np.cos(x)

# Using the default settings, use pyplot to plot  y1  and  y2  versus  x , 
#all on the same plot.

import matplotlib.pyplot as plt

plt.plot(x, y1, 'g--', x, y2, 'r:')
plt.show()


# Generate the same plots, but set the horizontal and vertical limits to be 
# slightly smaller than the default settings. In otherwords, tighten up the 
# plot a bit.


plt.plot(x, y1, x, y2)

plt.axis([-10,10, -1.2, 1.2])

plt.show()


# Generate the same plots using all settings from above, but now change the 
# color and thickness of each from the defaults. Play around with the values 
# a bit until you are satisfied with how they look.

plt.plot(x, y1, 'c1', x, y2, 'm1')

plt.axis([-10,10, -1.2, 1.2])



# Generate the same plots using all settings from above, but now add some 
# custom tickmarks with labels of your choosing. Which values would make sense 
# given the functions we are using?

plt.plot(x, y1, 'c1', x, y2, 'm1')

#plt.axis([-10,10, -1.2, 1.2])

plt.xticks([-6,-4,-2,0,2,4,6 ],[-360, -270,-180,-90,0, 90,180,270,360])


# Generate the same plots using all the settings from above, but now change 
# your plot spines so that they are centered at the origin. In other words, 
# change the plot area from a "box" to a "cross".


#plt.plot(x, y1, 'c1', x, y2, 'm1')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, 'c1', x, y2, 'm1')

plt.xticks([-6,-4,-2,0,2,4,6 ],[-360, -270,-180,-90,0, 90,180,270,360])

#fixing Spines
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


#Generate the same plots using all the settings from above, but now add a 
# legend, with labels sine and cosine, to your plot in a position of your 
# choosing.

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, 'c1', label = 'Sinx')
ax.plot( x, y2, 'm1', label = 'Cosinx')
plt.legend(loc ="best")

plt.xticks([-6,-4,-2,0,2,4,6 ],[-360, -270,-180,-90,0, 90,180,270,360])

#fixing Spines
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

##Question: on fig and ax 


# Now generate two more data sets,
# y3=sin(x)+sin(2x)
# y4=cos(x)+cos(2x)
# and add them to your plot, setting different color and line styles 
# (for example, dotted). Be sure to adjust your scales and legend as needed. 
# Also add a title to your plot.

y3 = np.sin(x) + np.sin(2*x)
y4 = np.cos(x) + np.cos(2*x)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, 'c1', label = 'Sinx')
ax.plot( x, y2, 'm1', label = 'Cosinx')
plt.legend(loc ="best")
ax.plot(x,y2, 'y-', label = "in(x)+sin(2x)" )
ax.plot(x, y4, 'g-', label = "cos(x)+cos(2x)")
plt.legend(loc ="best")
plt.title("Pretty Graphs")

## Q: which part displays the graph?

## More plot with real data

# Go to the R Data Repository and download, or load directly, the Aircraft 
# Crash data, load it into a Data Frame, and print the first few rows.
import pandas as pd
import matplotlib.pyplot as plt
air1 = pd.read_csv('/Users/Junna/Desktop/K2_intro_files/airAccs.csv')
air.head()

air = air1.dropna()

air.head()

# Generate a histogram for the number of deaths, using bin sizes of your 
# choice. Be sure to adjust the axis and to add a title to make your plot 
# aesthetically appealing.

air[['Dead']].describe()

plt.hist(air.Dead, bins = 20, rwidth = 1.2)
plt.title("Histogram")

# Make some plots of total number of deaths with respect to time, 
# making use of Pandas time series functionality. Again, be sure to make your 
# plot aesthetically appealing.

air.Date = pd.to_datetime(air.Date)

air_sub = air[['Date', 'Dead']]

air_grp = (air_sub.groupby("Date").sum().reset_index())

air_grp.plot('Date', 'Dead', color = 'pink')


# We're now going to add in some data from a different source to take a look 
# at the bigger picture in terms of number of passengers flying each year. 
# Head over to the World Bank Webpage and download the .csv version of the 
#data in the link. Clean it up and merge it with your original aircraft 
#accident data above. Call this merged data set data_all.

wb = pd.read_excel('/Users/Junna/Desktop/K2_intro_files/API_IS.AIR.PSGR_DS2_en_excel_v2_1310.xls',sheet_name = "Data")

#fixing column headers

header = wb.iloc[2]

wb = wb[3:]

wb.columns = header

#subsetting data

wb.shape
wb.head()

wb_subset = wb.ix[: , 4:63]
wb_subset.head()


##getting the right format
test = wb_subset.melt(var_name = "Date", value_name = "passenger_count")
test.head(20)

gb = test.groupby('Date')
pass_tot = gb.sum()
pass_tot.reset_index(inplace = True)
pass_tot.head()

air_grp['year'] = air_grp['Date'].astype(str).str[0:4]
pass_tot['year'] = pass_tot['Date'].astype(str).str[0:4] -> there must be a better way to do this



data_all = pd.merge(left = air_grp, right = pass_tot, left_on = "year",
                    right_on = "year", how = "inner")

data_all.info()

data_all['year'] = data_all['year'].astype(int)

# Using data_all, create two graphs to visualize how the number of deaths and 
# passengers vary with time, and, as always, make your plots as visually 
#appealing as possible.


plt.subplot(1,2,1)
plt.bar(data_all.year, data_all.Dead, align = 'center', color=(0.8, 0.4, 0.6, 0.6))
plt.title('Death by Year')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')


plt.subplot(1,2, 2)
plt.bar(data_all.year, data_all.passenger_count, align = 'center',
        color=(0.2, 0.8, 0.6, 0.6))
plt.title('Passengers per Year')
plt.xlabel('Year')
plt.ylabel('Number of Passengers')
plt.show()
 

# Make a pie chart representing the number of deaths for each decade. 
# Consult the pyplot documentation to play around with the settings a bit.

data_all.describe()

#i think there's a better way, will have to look
def decader(val):
    
    if val >= 1960 and val < 1970:
        return 1960
    
    elif val >= 1970 and val < 1980:
        return 1970
    
    elif val >= 1980 and val < 1990:
        return 1980
    
    elif val >= 1990 and val < 2000:
        return 1990
    
    elif val >= 2000 and val < 2010:
        return 2000
    
    elif val >= 2010 and val < 2020:
        return 2010

data_all['Decade'] = data_all['year'].apply(decader)


##grouing by decade for pie chart

gb = data_all.groupby('age_cat')
df_mean = gb.mean()
df_mean.head()
print(df_mean)

gb = data_all.groupby('Decade')
gb_sum = gb.sum()
gb_sum.reset_index(inplace = True)
gb_sum.head()

gb_sum['Decade'] = gb_sum['Decade'].astype(str)
gb_sum.info()

plt.pie(gb_sum['Dead'], labels= gb_sum['Decade'] )
plt.axis('equal')
plt.show()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
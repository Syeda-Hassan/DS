#Download the free1.csv from the R Data Repository and save it to the same directory as this notebook. Then import into your environment as a Data Frame. Now read free2.csv directly into a Data Frame from the URL.

import pandas as pd

free_1 = pd.read_csv("/Users/Junna/Desktop/K2_intro_files/2_scipy/2_assignments/free1.csv")

free_2 = pd.read_csv("/Users/Junna/Desktop/K2_intro_files/2_scipy/2_assignments/free2.csv")


##didnt work using the url
free2 = None
try:
 csv_url = "https://vincentarelbundock.github.io/Rdatasets/datasets.html/free2.csv"
 free2 = pd.read_csv(csv_url, index_col=0)
 free2 = free2.head()
except IOError as e:
    print(e)

##Combine your free1 Data Frame with free2 into a single Data Frame, 
#named free_data, and print the first few rows to verify that it worked correctly. 
#From here on out, this combined Data Frame is what we will be working with. (Hint: 
#use the concat method).

free_data = pd.concat([free_1, free_2], ignore_index = True)
    
#Print the last 10 rows.

free_data[-10:]

free_data.tail(10)

#Rename the first column (currently unamed), to id. Print the column names to 
#verify that it worked correctly.

free_data.rename(columns = {'Unnamed: 0' : 'id'}, inplace = True)

free_data.columns

#What are the number of rows and columns of the Data Frame?

free_data.shape

#What are the data types of each column? 
#Can quantities like the mean be calculated for each columm? 
#If not, which one(s) and why?

free_data.dtypes

## -- no, mean can't be calculated for categorical columns like country

#Print out the first 5 rows of the country column.


free_data['country'].head(5)

#How many unique values are in the country column?

free_data.country.unique()


#Print out the number of occurences of each unique value in the country column.

free_data.country.value_counts()

#Summarize the dataframe.

free_data.describe()

free_data.info()

#Were all columns included in the summary? If not, print the summary again, 
#forcing this column to appear in the result.

# All columns were included, any unique case i should know about?


#Print rows 100 to 110 of the free1 Data Frame.

free_1.loc[99:109,]


#Print rows 100 to 110 of only the first 3 columns in free1 using only indices.

free_1.iloc[99:109, :3]

#Create and print a list containing the mean and the value counts of each column 
#in the data frame except the country column.

colnames = free_data.columns[free_data.columns != 'country']

[free_data[colnames].count(), free_data[colnames].mean(axis = 0)]

#Create a Data Frame, called demographics, using only the columns sex, age, and educ 
#from the free1 Data Frame. 
#Also create a Data Frame called scores, using only the columns v1, v2, v3, v4, v5, v6 f
#from the free1 Data Frame

demographics = free_1[['sex','age', 'educ' ]]
demographics.head()

scores = free_1[['v1','v2', 'v3', 'v4', 'v5', 'v6']]


#Loop through each row in scores and grab the largest value, in the v_ columns, 
#found in each row and store your results in two lists containing the value and column 
#name it came from. For example, row 0 is 
# {'v1': 4, 'v2': 3, 'v3': 3, 'v4': 5, 'v5': 3, 'v6': 4}
# the values ('v4', 5) should be added to your two lists.

scores.apply(lambda x: ( x.idxmax(), x.max()), axis = 1).tolist()

#or 

res_val = []
res_idx = []
for idx, row in scores.iterrows():
    res_val.append(row.max())
    res_idx.append(row.idxmax())

print(res_val)
print(res_idx)


#Create a new Data Frame with columns named cat and score from your results in part (16),
# for the column with the largest score and the actual score respectively.

score_freq = pd.DataFrame(list(zip(res_idx, res_val)), columns = ['category', 'score'])
score_freq

#Using the Data Frame created in part (17), print the frequency of each column being the 
#max score.

score_freq['category'].value_counts()

##############################################################################
##SORTING AND GROUPING DATA

#Using the free1.csv downloaded above, import it as a Data Frame named free_data, 
#rename the first column to id, and print the first few rows.

free_data = free_1

free_data.columns

free_data.rename(columns = {'id' : 'id'}, inplace = True)

free_data.head()

#Sort free_data by country, educ, and then by age in decending order, 
#modifying the original Data Frame.

people.sort_values(by="age", inplace=True)

free_data.sort_values(by = ['country', 'educ', 'age'], ascending = False, inplace = True)

free_data.head()

#Create a new Data Frame called uni containing only rows from free_data which 
#indicate that the person attended university or graduate school. 
#Print the value counts for each country.

#don't understand edu colum
uni = free_data[['educ', 'country']][free_data.educ >= 1]

uni['country'].value_counts()


#Create a list of three Data Frames for those who are less than 25 years old, 
#between 25 and 50 years old, and older than 50.

[below_25, betn_25_50, above_50] = [free_data[free_data['age'] <25], 
     free_data[(free_data['age'] >= 25 )| (free_data['age'] <= 50)], 
     free_data[free_data['age'] > 50]]

betn_25_50.tail() # -> range not working?

above_50.tail()

#########
test = free_data[(free_data.age >50) | (free_data.age == 50)]
test


#Using a for loop, create a list of 3 Data Frames each containing only 
#one of the 3 countries.

d = []
for name in list(free_data.country.unique()):
    d.append(free_data.loc[free_data.country == name])


##Create a list of age categories, labled 0, 1, and 2 for each row for the 
#three groups made in part (4). Attach this list to the free_data 
#dataframe as a column named age_cat.

 
##first method:
    
row_list = []

for value in free_data['age']:
    if value < 25:
        row_list.append(0)
    elif value >= 25 and value <= 50:
        row_list.append(1)
    elif value > 50:
        row_list.append(2)
    elif np.isnan(value):
        row_list.append(None)
    else:
        row_list.append(None)

free_data['age_cat'] = row_list

### I have learned that loops are inefficient:
def age_categorizer(value):
    if value < 25:
        return 0
    elif value >= 25 and value <= 50:
        return 1
    elif value > 50:
        return 2

    return None

free_data['age_cat'] = free_data['age'].apply(age_categorizer)

print(free_data.tail())

        
# Print the mean for all columns for each age_cat using groupby.
gb = free_data.groupby('age_cat')
df_mean = gb.mean()
df_mean.head()
print(df_mean)

# Print the mean education for each age_cat using groupby.

print(df_mean['educ'])

# Print summary statistics for each column for those with an education greater 
# than or equal to 5, grouped by age_cat.
df2 = free_data.loc[free_data.educ >= 5, :]
gb2 = df2.groupby('age_cat')
print(gb2.describe())


# Which of the vignette has the largest mean score for each education level?

gb_edu = free_data.groupby('educ')

df_mean = gb_edu.mean()
df_v = df_mean[['v1', 'v2', 'v3', 'v4', 'v5', 'v6']]

df_v.apply(lambda x: x.idxmax(), axis=1)

# What about the median?

df_median = gb_edu.median()
df_v2 = df_median[['v1', 'v2', 'v3', 'v4', 'v5', 'v6']]
df_v2.apply(lambda x: x.idxmax(), axis = 1)

# Which country would you say has the most freedom of speech? 
# Be sure to justify your answer quantitatively.

gb_cont = free_data.groupby('country')

cont_mean = gb_cont.mean()

cont_mean

df_v3 = cont_mean[['v1', 'v2', 'v3', 'v4', 'v5', 'v6']]

df_v3.apply(lambda x: x.idxmin(), axis = 1)

#Is there a difference of opinion between men and women regarding freedom 
# of speech? If any, does this difference manifest itself accross the 
# different countries? Accross education levels? Be sure to justify 
# your answers quantiatively.

free_data.columns

gb = free_data.groupby(['sex', 'country', 'educ'])

gb_mean = gb.mean()

gb_mean

### PART 3

# Using the free1.csv downloaded above, import it as a Data Frame named 
#free_data and rename the first column to id.

free_1.head()

free_1.rename(columns = {'Unnamed: 0' : 'id' }, inplace = True)

# Create a dataframe named free_sub, consisting of the id, country, 
 #and y columns from free_data.
 
free_sub = free_1[['id', 'country', 'y']] 
 
# Create a new Data Frame called ed_level, consisting of the id and three 
# categories of education levels, labeled high, med, and low, for ranges of 
# your choosing. Do this using a for loop.

free_1.educ.describe()

def educ_level(val):
    if val <= 4:
        return 'low'
    elif val > 4 and val <= 6:
        return 'med'
    elif val == 7:
        return 'high'
    
    return None 
    
ed_level = free_1[['id', 'educ']] 
ed_level['ed_cat'] = ed_level['educ'].apply(educ_level)

ed_level.head()

# Merge free_sub and ed_level together. Which column should the merge be 
# performed on? Do this using both the concat() and merge() functions.

concat_df = pd.concat([free_sub, ed_level], ignore_index = True)

merged_df = pd.merge(left = free_sub, right = ed_level, on = 'id')

concat_df.head()
free_sub.head()
ed_level.head()

merged_df.info()

# Use the append() function to join together free_sub and ed_level. 
# Are the results the same as in part (4)? If not, how could you reproduce 
# the result append() by using concat() or merge()?

free_sub.append(ed_level)

# -> same result as concat?


# Use numpy to generate two lists 100 random floats labeled y1 and y2. 
# Now create a sequence of integers on the range 0-100 labeled x1 and a 
# sequence of integers on the range 50-150 labeled x2. Create two DataFrames, 
# dat1 and dat2 consisting of x1 and y1, and x2 and y2 respectively, 
# but having labels x, y1, and x, y2. Use merge() to join these two 
# Data Frames together, on x, using both an inner and outer join. 
# What is the difference between the two joins?

import numpy as np
import random 

y1 = np.random.rand(100) # -> not a list though?
y2 = np.random.rand(100)

x1 = random.sample(range(1,101),100)
x2 = random.sample(range(50,151), 100)

dat1 = pd.DataFrame({'x1': x1, 'y1': y1})

dat2 = pd.DataFrame( {'x2': x2, 'y2':  y2})


pd.merge( left = dat1, right = dat2, left_on = 'x1' , right_on = 'x2', 
         how = 'inner')

## inner join leaves only rows matching x1 == x2
## outer join keeps everything, producing bunch of Nans

# Create a Data Frame, called scores consising of only the y and v_ columns 
# from free_data.

#v_col = [col for col in free_data if col.startswith('v')]

# -> didn't work ^

scores = free_data.filter( regex = '[y - v]') 
scores.head()

 ## didnt get rid of country column??
 
scores.drop('country',  axis = 1, inplace = True)


# Using a for loop(s), compute the sum and mean for each column in scores.

scores.info()

for col in scores:
    print(col, ":", "mean", scores[col].mean())
    print("sum", scores[col].sum())
    
# Using the apply() function, compute the sum and mean for each column in scores.

scores.apply(lambda x: x.mean())
scores.apply(lambda x: x.sum())


# Using the apply() function, label each column in scores as either 
# high, med, or low by first computing the mean for each column and 
# assigning the categories at values of your choosing. Do this by writing a 
# single function you can call with apply().

def mean_cat(df):
    for col in df:
        if df[col].mean() > df.mean():
            return "high"
        elif df[col].mean() < df.mean():
            return "low"
        else:
            return "med"
        
scores.apply(mean_cat)




















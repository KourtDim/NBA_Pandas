# NBA Pandas Readme

The NbaStats.py script functions in a variety of ways:

It creates a pandas dataframe - df_totals - which contains the total stats for every player that participated in the 2019/2020 NBA season. This dataframe can then be used for a variety of data analysis and visualization on the given data. 

After creating the pandas dataframe  a variety of functions are defined that the use can use in order to obtain statistical insights on specific querries. 

E.g. using the function - describe - which takes as a variable the name of one statistical category from the dataset: describe("STL") gives:

####
Descriptive Statistics for:  STL 

The Mean for  STL  is:  22.58
The Median for  STL  is:  19.0
The Mean Absolute Deviation for  STL  is:  16.055 

Top Ten Players in:  STL 

Player
Ben Simmons         105.0
Kris Dunn           101.0
Andre Drummond       94.0
Chris Paul           79.0
Robert Covington     77.0
Fred VanVleet        77.0
Jimmy Butler         75.0
James Harden         75.0
Dejounte Murray      74.0
Zach LaVine          73.0
Name: STL, dtype: float64

####



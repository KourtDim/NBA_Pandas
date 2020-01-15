
### Import Libraries

import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Create a variable for the selected url
url_totals = 'https://www.basketball-reference.com/leagues/NBA_2020_totals.html'
url_pergame = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"
url_per36 = "https://www.basketball-reference.com/leagues/NBA_2020_per_minute.html"
#Using the urlopen function to read the url in its html form
#uClient = urlopen(url)

#Read the webpage
#url_html = uClient.read()
#uClient.close()

#Parsing the html code
#url_soup = soup(url_html, 'html.parser')

#Create the Dataframe

#Using pandas read_html function on a url creates a list of all the html tables in the given url
url_df_totals = pd.read_html(url_totals)
url_df_pergame = pd.read_html(url_pergame)
url_df_per36 = pd.read_html(url_per36)
#Create our pandas dataframe by selecting from the list the table we want to analyze
df_totals = url_df_totals[0]
df_pergame = url_df_pergame[0]
df_per36 = url_df_per36[0]
#Check if all works
#df.head(10)

# Check the table type 
#df_type = type(df)
#df_type

#Check number of rows and length
#df_shape = df.shape
#df_shape

#Check columns names
#df_columns = df.columns
#print(df_columns)

#Check table's datatypes
#df_dtype = df.dtypes
#df_dtype

#There are issues with the data types of the columns, in order to solve this issue we use the astype() function
#First create a list of the columns that need conversion

cols=["Rk","Age","G","GS","MP","FG","FGA","FG%","3P","3PA","3P%","2P","2PA","2P%","FT","FTA","FT%","ORB","DRB","TRB","AST","STL","BLK","TOV","PF","PTS"]
df_totals = df_totals.fillna(0)
df_totals = df_totals[df_totals["Player"] != "Player"]
df_totals = df_totals.drop_duplicates(subset="Player")

df_pergame = df_pergame.fillna(0)
df_pergame = df_pergame[df_pergame["Player"] != "Player"]
df_pergame = df_pergame.drop_duplicates(subset="Player")

df_per36 = df_per36.fillna(0)
df_per36 = df_per36[df_per36["Player"] != "Player"]
df_per36 = df_per36.drop_duplicates(subset="Player")
# Change the dtypes:

df_totals[cols]= df_totals[cols].astype("float")
df_pergame[cols]= df_pergame[cols].astype("float")
df_per36[cols]= df_per36[cols].astype("float")
#df_pergame[cols]= df_pergame[cols].astype("float")
#df_per36[cols]= df_per36[cols].astype("float")

#print(df_totals.dtypes)
#print(df_pergame.dtypes)
#print(df_per36.dtypes)

# Data Cleaning Process
# Now that the dtypes are ok we can analyse the data, but before that we have to look for empty cell NaN and similar values
# First we check for missing values with isnull function

#df_totals.isnull().sum()
# from the results we see there are missing values and we need to fill them 

#df_totals = df_totals.fillna(0)
# We see now that the empty values are replaced.
#df.count()

# We found out that the categories row was repeating itself throughout the text so we had to get rid of 24 rows
##df.loc[df['Player'] == "Player"]
#df_totals = df_totals[df_totals["Player"] != "Player"]
#df.loc[df['Player'] == "Player"]
# Drop all duplicated rows and keep the first occurence
#df_totals = df_totals.drop_duplicates(subset="Player")

#Find All Players that are above league average in 9 categories
#players_above_average = df.loc[(df["FG%"]>df["FG%"].mean())& (df["FT%"]>df["FT%"].mean()) & (df["PTS"]>df["PTS"].mean())& (df["AST"]>df["AST"].mean())&(df["TRB"]>df["TRB"].mean())&(df["STL"]>df["STL"].mean())&(df["BLK"]>df["BLK"].mean())&(df["TOV"]<df["TOV"].mean()) ]

#Find All Players with a 50-40-90 shooting percentage
#player_50_40_90 = df.loc[(df["FG%"]>0.49) & (df["FT%"]>0.89) &(df["3P%"]>0.39)]
#print(players_above_average)


topten_totals={}
for i in df_totals.columns:
     if df_totals[i].dtype == "float64":
          topten_totals[i]= pd.DataFrame(df_totals[["Player",i]].nlargest(10,[i]))

y = topten_totals["STL"]["STL"]
x = topten_totals["STL"]["Player"]

plt.bar(x,y,color="#99cc00",label="Bar")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Top 10 Steals Totals")
plt.legend()
plt.show()




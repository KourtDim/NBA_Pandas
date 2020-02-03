####      IMPORT LIBRARIES              ####

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import mplcursors

#
##
###
####      CREATE THE DATAFRAME          ####

""" 1. Create a variable where the url string is stored, the data that will be used are the Nba Totals
     for 2019/2020 season , this dataset contains the total production of each NBA player that has played
     in any game of the forementioned season"""

url = ("https://www.basketball-reference.com/leagues/NBA_2020_totals.html")

""" 2. Create the Dataframe using the url variable. The Pandas library contains the function read_html()
     which finds all the html tables in a given webpage and creates a list of pandas dataframes """

df_totals = pd.read_html(url)


#
##
###
####      Data Cleaning & Validation    ####

#------------------------------------------#
""" 1.In order to confirm that the variable contains 1 table and that it has taken the correct data type
     the following if statement is used """

type_check = isinstance(df_totals[0], pd.DataFrame)

if len(df_totals) > 1:
     print("Error: More than one html table inside the given url")
elif len(df_totals) < 1:
     print("Error: No html table inside the given url")
elif len(df_totals) == 1:
     if type_check == True:
          df_totals = df_totals[0]
          print("Type Check: OK")
     else:
          print("Error: The Dataframe is not of the correct type.")


          
#------------------------------------------#
          
""" 2. Check if there are duplicated values in the Dataset based on Player column and drop duplicated values"""

df_totals.drop_duplicates(subset="Player",keep="first",inplace=True)

if df_totals.Player.nunique() == len(df_totals.Player.unique()):
     print("Duplicate Check: OK")
else:
     print("Error: Your DataFrame contains duplicated values")

df_totals = df_totals[df_totals["Player"] != "Player"]
df_totals.to_csv("removeduplicates.csv")
#------------------------------------------#
     
""" 3. After removing duplicated player rows it appears that some columns contain only digits but their dtype is
     object. In order to fix this the follow loop will be used """

##   Create an empty list
cols = []

##   Create a for loop that checks if all values of a column are numeric and save those columns to cols
df_totals.applymap(str)


for i in df_totals:
     a = df_totals[i].str.isnumeric()
     aun = a.unique()
     if len(aun) == 1 and aun[0] == True:
          cols.append(i)

##   Convert the filtered columns to float

df_totals[cols]= df_totals[cols].astype("float")

colb = ["FG%","3P%","2P%","eFG%","FT%"]
df_totals[colb]= df_totals[colb].astype("float")

print("Dftype Check: OK")

#------------------------------------------#


#
##
###
####           SET INDEX                ####

""" 1. In order to have better results in the data analysis it is necessary to set a meaningfull index , in this case the only unique identifier
     is the Player's name """

df_totals.set_index("Player",inplace=True)

#------------------------------------------#


#
##
###
####           DROP COLUMNS             ####

""" 2. The Rk column is uneccessary for the analysis therefore is can be dropped from the DataFrame"""

df_totals.drop(columns="Rk",inplace=True)

#------------------------------------------#


#
##
###
####           Data Analysis  `         ####

""" For the Data Analysis a variety of functions will be defined that will be conducting a specific type of statistical analysis """

columns = []
for i in df_totals:
     columns.append(i)
     
#    1. Descriptive Statistics

def describe(category):
     df_totals[category].describe()
     print("Descriptive Statistics for: " , category, "\n")
     print("The Mean for ", category, " is: ", round(df_totals[category].mean(),3))
     print("The Median for ", category, " is: ", round(df_totals[category].median(),3))
     print("The Mean Absolute Deviation for ", category, " is: ", round(df_totals[category].mad(),3),"\n")

     print("Top Ten Players in: " , category, "\n")
     print(df_totals[category].nlargest(10))

#    2. Scatter Plots
##   2.1 2 Dimensional scatter plot

def scatter_2D(catA,catB):
     if df_totals[catA].sum() > df_totals[catB].sum():
          x= df_totals[catB]
          y= df_totals[catA]
          df_totals["Ratio"] = df_totals[catA]/df_totals[catB]
          plt.xlabel(catB)
          plt.ylabel(catA)
          
               
     elif df_totals[catA].sum() < df_totals[catB].sum():
          x= df_totals[catA]
          y= df_totals[catB]
          df_totals["Ratio"] = df_totals[catB]/df_totals[catA]
          plt.xlabel(catA)
          plt.ylabel(catB)
          
     ratio= df_totals["Ratio"]
     
     plt.style.use('seaborn')
     a=plt.scatter(x,y,s=ratio*25,c=ratio,cmap="summer", edgecolor='black',linewidth=1,alpha=0.5)
     cbar= plt.colorbar()
     mplcursors.cursor(a)
     cbar.set_label("Ratio")

     plt.title("Scatter Plot")
     plt.show()
     """
        c= df_totals[catA].corr(df_totals[catB],method="spearman")
        ax=df_totals.plot(kind="scatter",x=catA,y=catB,color="#94b8b8",grid=True)
        ax.set_facecolor("#ffffe6")
        plt.show()
     """
"""
#    2.2 Fantasy Correlograph
def scatter():
     import seaborn as sns
     sns.set(color_codes=True)
     sns.pairplot(df_totals[["PTS","AST","STL","BLK","3P","TOV","FG%","FT%","TRB"]])
     plt.show()
"""
#    3 Histogram

def histogram(cat):
     import seaborn as sns
     sns.set(color_codes=True)
     sns.distplot(df_totals[cat])
     plt.show()

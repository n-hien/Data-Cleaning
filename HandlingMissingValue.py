import pandas as pd
import numpy as np 

#read the data
permits = pd.read_csv("Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0) 

#get the number of missing data points per column
missing_values_count = permits.isnull().sum()

# total missing values 
total_cells =np.product(permits.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells)*100

#figure out why the data is missing
#is this value missing because it wasn't recorded or because it dosn't exist?

#Drop missing values rows
permits_with_na_dropped = sf_permits.dropna()

#Drop missing values: columns
#Create a new DataFrame called sf_permits_with_na_dropped that has all of the columns with empty values removed.
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

#How many columns were removed from the original sf_permits DataFrame?
column_in_original = sf_permits.shape[1]
column_with_na_dropped= sf_permits_with_na_dropped.shape[1]
dropped_columns = column_in_original - column_with_na_dropped

#Filling in missing values automatically
#replace all the NaN's in the sf_permits data with the one that comes directly after it and then replacing any remaining NaN's with 0
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill',axis=0).fillna(0)
#EXERSISE 6 

#Task 1 
import pandas as pd 
wages=pd.read_csv('wages.csv')
wages.head(n=5)

#Task 2
import pandas as pd 
iris=pd.read_csv('iris.csv')
iris.shape
#2a
iris.iloc[148:,3:]
#2b
from collections import Counter 
Species=iris.iloc[:,4:]

#2c
iris.iloc[:,1:2]>3.5

#2d

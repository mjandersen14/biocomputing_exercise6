#EXERSISE 6 

#Task 1 
import pandas as pd 
wages=pd.read_csv('wages.csv')
wages.head(n=5)

#Task 2
import pandas as pd 
iris=pd.read_csv('iris.csv')
iris.shape

#2a : print the last 2 rows in the last 2 columns to the Python terminal
iris.iloc[148:,3:]

#2b : get the number of observations for each species included in the data set
species=iris.iloc[:,4:]
species.shape

specieslist=iris['Species'].tolist()

from collections import Counter
Counter(specieslist)

#2c : get rows with Sepal.Width > 3.5
iris.loc[iris['Sepal.Width']>3.5]
    
#2d : write the data for the species setosa to a comma-delimited file named setosa
setosa=iris.loc[iris['Species']=='setosa']
setosa.to_csv(path_or_buf='setosa.csv')

#2e : calculate the mean, minimum, and maximum of Petal.Length for observations from virginica
def iris_calcs():
    virginica=iris[iris['Species']=='virginica']
    petalL=virginica['Petal.Length']
    minimmum=min (petalL)
    maximmum=max (petalL) 
    total=sum (petalL)
    average=total/50
   
    return minimmum, maximmum, average

iris_calcs()

















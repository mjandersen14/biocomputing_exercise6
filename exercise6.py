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
count=0
cat while read line
do
    if echo $line | grep $stringChoice; then
        count=$[ count + 1 ]
done
echo "Finished processing file"


#2c : get rows with Sepal.Width > 3.5
iris.iloc[:,1:2]>3.5

#2d : write the data for the species setosa to a comma-delimited file names ‘setosa.csv’

#2e : calculate the mean, minimum, and maximum of Petal.Length for observations from virginica

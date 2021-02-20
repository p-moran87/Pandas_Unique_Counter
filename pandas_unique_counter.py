# script to parse a csv or text file with two columns: name of file and events, and count the number of occurences of events 

import pandas

df = pandas.read_csv('test.csv')

# Remove the last 2 characters for each item in column no. 1

df['Name'] = df['Name'].map(lambda x: str(x)[:-2])

print(df.groupby('Name').apply(lambda column: column.sum().sum()).sort_values(ascending=False))

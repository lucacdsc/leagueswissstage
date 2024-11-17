import pandas as pd

numbers = [1,7,2]

my_series = pd.Series(numbers,index=['Number1','Number2','Number3'])
print(my_series)
print(my_series['Number1'])

data = {
  'calories': [420,380,390],
  'duration':[50,40,45]
}

my_dataframe = pd.DataFrame(data,index=['day1','day2','day3'])
print(my_dataframe)

print(my_dataframe.loc['day1'])
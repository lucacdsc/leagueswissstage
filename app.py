import json
import numpy as np
import pandas as pd
import yfinance as yf




# luca_salary = [1212,2500,3000]
# nick_salary = [2600,2800,2800]
# tom_salary =  [2300,2500,2500]

# base_salary = np.array([luca_salary,nick_salary,tom_salary])
# print(base_salary)

# luca_bonus = [200,300,400]
# nick_bonus = [400,200,150]
# tom_bonus = [100,300,230]

# bonus = np.array([luca_bonus,nick_bonus,tom_bonus])
# print(bonus)
# salary_bonus = base_salary + bonus
# print(type(salary_bonus))
# print(salary_bonus)

# data = ['Gon','Meruem','Netero','Killua']
# names = pd.Series(data)

# print(names)

# tkr = yf.Ticker('TSLA')
# hist = tkr.history(period='5d')
# hist = hist.drop('Dividends', axis = 1)
# hist = hist.drop('Stock Splits', axis = 1)
# hist = hist.reset_index()

# print(hist)


data = [
{'Empno':9001,'Salary':3000},
{'Empno': 9002, 'Salary':2800},
{'Empno': 9003,'Salary':2500}
]

json_data = json.dumps(data)
salary = pd.read_json(json_data)
salary = salary.set_index('Empno')
# print(salary)
      
data2 =[
  ['9001','Luca','Technical support'],
  ['9002','Teste','Dev'],
  ['9003','Teste2','Qa']
]

worker_salary = pd.DataFrame(data2, columns=['Id','Name','Role'])
column_types = {'Id':int,'Name': str, 'Role':str}
worker_salary = worker_salary.astype(column_types)
worker_salary = worker_salary.set_index('Id')
# print(worker_salary)

emps_salary = worker_salary.join(salary)
print(emps_salary)
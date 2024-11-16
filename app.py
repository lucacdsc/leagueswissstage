import json
import numpy as np
import pandas as pd
import yfinance as yf




# # luca_salary = [1212,2500,3000]
# # nick_salary = [2600,2800,2800]
# # tom_salary =  [2300,2500,2500]

# # base_salary = np.array([luca_salary,nick_salary,tom_salary])
# # print(base_salary)

# # luca_bonus = [200,300,400]
# # nick_bonus = [400,200,150]
# # tom_bonus = [100,300,230]

# # bonus = np.array([luca_bonus,nick_bonus,tom_bonus])
# # print(bonus)
# # salary_bonus = base_salary + bonus
# # print(type(salary_bonus))
# # print(salary_bonus)

# # data = ['Gon','Meruem','Netero','Killua']
# # names = pd.Series(data)

# # print(names)

# # tkr = yf.Ticker('TSLA')
# # hist = tkr.history(period='5d')
# # hist = hist.drop('Dividends', axis = 1)
# # hist = hist.drop('Stock Splits', axis = 1)
# # hist = hist.reset_index()

# # print(hist)


# salarios = [
# {'Empno':9001,'Salary':3000},
# {'Empno': 9002, 'Salary':2800},
# {'Empno': 9003,'Salary':2500},
# {'Empno': 9004, 'Salary': 2750}
# ]

# json_data = json.dumps(salarios)
# salario = pd.read_json(json_data)
# salario = salario.set_index('Empno')
# # print(salario)
      
funcionarios =[
  ['9001','Luca','Technical support'],
  ['9002','Teste','Dev'],
  ['9003','Teste2','Qa']
]

funcionario = pd.DataFrame(funcionarios, columns=['Id','Name','Role'])
column_types = {'Id':int,'Name': str, 'Role':str}
funcionario = funcionario.astype(column_types)
funcionario = funcionario.set_index('Id')
# print(funcionario)

novo_funcionario = pd.Series({'Name':'Teste3','Role':'sales'}, name = '9004')
funcionario = pd.concat([funcionario, novo_funcionario.to_frame().T])
# print(funcionario)

# salario_funcionario = funcionario.join(salario)
# print(salario_funcionario)

data = [[2608,9001,35],[2617,9001,35],[2620,9001,139],[2621,9001,95],[2626,9002,218]]

orders = pd.DataFrame(data, columns=['Ano','Id','Total'])
print(orders)


pedidos_dos_funcionarios = funcionario.merge(orders, how = 'inner', left_on='Id', right_on ='Id').set_index('Ano')
print(pedidos_dos_funcionarios)
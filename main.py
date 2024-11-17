#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('data/champions.csv')
df.head(50)
# %%
df.info()
df.describe()
# %%
champions = df['Champion'].values

for champion in champions:
  print(f'\n Champion: {champion}')

# %%
# Filtre os campeões com mais de 50% de Presence.
df['Presence'] = df['Presence'].str.replace('%','').astype(float)

champions_over_50_percent_presence = df['Presence'] > 50
df[champions_over_50_percent_presence]

# %%
# Ordenar os campeões por número de Picks do maior para o menor.
df.info()
champions_most_pick = df.sort_values(by='Picks', ascending=False)
champions_most_pick

# %%
#Filtre os campeões com Winrate maior que 60%.
df['Winrate'] = df['Winrate'].str.replace('%','').astype(float)

champions_over_60_percent_winrate = df['Winrate'] > 60
df[champions_over_60_percent_winrate]
# %%
#Liste os 5 campeões com a maior KDA.
df.info()
df['KDA'].dtype
df['KDA'] = pd.to_numeric(df['KDA'], errors='coerce')
df['KDA'].dtype

df.nlargest(5,'KDA')

# %%
#Quais são os campeões com os maiores valores de DPM?
df['DPM'].dtype
df.nlargest(3,'DPM')
# %%
# Liste os campeões com GD@15 positivo (ganhando mais ouro aos 15 minutos do que seus adversários).
df.info()
champions_winning_lane_phase = df['GD@15'] > 0
df[champions_winning_lane_phase].sort_values(by='GD@15',ascending=False)
# %%
#Adicione uma nova coluna chamada - Efficiency, calculada como - Efficiency = DPM / GPM e exiba os cinco campeões com a maior eficiência.
df.info()
df['Efficieny'] = np.divide(df['DPM'],df['GPM'], out=np.zeros_like(df['DPM'],dtype=float), where= df['GPM'] != 0).round(2)
selected_columns = df[['Champion','DPM','GPM','Efficieny']]
selected_columns.head(6)
# %%
mean_csd15 = df.groupby('Picks')['CSD@15'].mean()
mean_xpd15 = df.groupby('Picks')['XPD@15'].mean()
max_gd15 = df.groupby('Picks')['GD@15'].max()
# %%

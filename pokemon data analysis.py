# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('datasets/pokemon.csv')
df

# %%
df.shape

# %%
df.describe()

# %%
df.info()

# %%
df = df[['name', 'type1', 'type2', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'generation', 'is_legendary']]

# %%
df.loc[:, 'total'] = df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].sum(axis=1)

df.insert(3, 'total', df.pop('total'))
df

# %%
df['type1'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='tab20c', figsize=(10, 8))

# %%
df['total'].plot(kind='hist', figsize=(10, 8))

# %%
df['total'].plot(kind='box', vert=False, figsize=(10, 5))

# %%
df['is_legendary'].value_counts().plot(kind='pie', autopct='%1.1f%%', cmap='Set3', figsize=(10, 8))

# %%
sns.boxplot(data=df, x='attack')

# %%
df.head(1)

# %%
df.loc[df['attack'] > 150]

# %%
df.loc[df['speed'] <= 10]

# %%
slow_pokemons_df = df.loc[df['speed'] <= 10]
slow_pokemons_df

# %%
df.loc[df['sp_defense'] <=25]

# %%
(df['sp_defense']<=25).sum()

# %%
df.info()

# %%
df['is_legendary'].sum()

# %%
df_legendary = df.loc[df['is_legendary'] == True]
df_legendary


# %%
egdf = pd.DataFrame([True, False, True, True])
~egdf

# %%
ax = sns.scatterplot(data=df, x='defense', y='attack')
ax

# %%
df.head()

# %%
df.sort_values(by=['defense', 'attack'], ascending=[False, True])

# %%
df['type1'].unique()

# %%
df[(df['type1'] == 'fire') & (df['type2']=='flying')]

# %%
df.query("`type1` == 'fire' and `type2` == 'flying'")

# %%
df.query("`type1` == 'fire' and not `type2` == 'flying'")

# %%
df['type1'].value_counts()

# %%
((df['type1'] == 'fire') & (df['type2'] == 'flying')).sum()

# %%
df.query("`type1`=='poison' or `type2`=='poison'")

# %%
df[(df['type1']=='poison') | (df['type2']=='poison')]


# %%
df.query("`type1`=='poison' or `type2`=='poison'").shape

# %%
df[(df['type1']=='poison') | (df['type2']=='poison')].shape

# %%
df.sort_values('defense', ascending=False)[:1]

# %%
# conver the 1 and 0 to True and False
df['is_legendary'] = df['is_legendary']==1

# the right way to do it is
df.iloc[:, 'is_legendary'] = df['is_legendary']==1

# %%
df.loc[df['is_legendary'], 'type1'].value_counts().plot(kind='bar')

# %%
df.loc[(df['type1']=='water') & df['generation'].isin([1, 2, 3])].sort_values('total', ascending=False)

# %% [markdown]
# Most powerful dragon in last 2 generation

# %%
df[((df['type1']=='dragon') | (df['type2']=='drason')) & df['generation'].isin([6, 7])].sort_values('total', ascending=False)

# %%
df.query("(`type1`=='dragon' or `type2`=='dragon') and `generation` in [6, 7]")

# %%
df[(df['attack']>100) & (df['type1']=='fire')]

# %%
df.query("`type1`=='fire' and `attack`>100")

# %%
water_flying_df = df.query("`type1`=='water' and `type2`=='flying'")
water_flying_df

# %%
legendary_fire_df = df.loc[(df['type1']=='fire') & df['is_legendary'], ['name', 'attack', 'generation']]
legendary_fire_df

# %%
bottom_5 = df['speed'].quantile(.05)
top_5 = df['speed'].quantile(.50)
bottom_5, top_5

# %%
df.loc[(df['speed']<bottom_5) | (df['speed']>top_5)] 

# %%
df.query(
    "speed < @bottom_5 or speed > @top_5"
)

# %%
df.loc[df['is_legendary']].sort_values(['attack', 'defense'], ascending=False).head(20)

# %%




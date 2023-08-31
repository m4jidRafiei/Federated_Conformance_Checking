import pandas as pd

df = pd.read_csv('sim_log.csv', sep=';')
df_collaborative = df[(df['Output'].notna()) | (df['Input'].notna())]


df_collaborative.to_csv('collaborative_log_.csv')

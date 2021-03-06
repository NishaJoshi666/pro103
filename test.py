import pandas as pd
import plotly.express as px

df = pd.read_csv('copy.csv')
fig = px.scatter(df,x='date',y='cases',color='country',title='COVID DATA')
fig.show()
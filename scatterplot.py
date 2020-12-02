import pandas as pd

import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df, x="student_id", y= "level", color= "attempt", size_max= 60)

fig.show()
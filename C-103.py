import pandas  as pd
import plotly.express as px

#df = pd.read_csv("/Users/adityadeonarayan/Desktop/whjr/C-99/csv files/line_chart.csv")
#fig = px.line(df,x="Year",y="Per capita income",color="Country",title = "Per capita income")




#df = pd.read_csv("/Users/adityadeonarayan/Desktop/whjr/C-99/csv files/data.csv")
#fig = px.bar(df,x= "Country",y ="InternetUsers")


df = pd.read_csv("/Users/adityadeonarayan/Desktop/whjr/C-99/csv files/data.csv")
fig = px.scatter(df, x = "Population", y= "Per capita",size= "Percentage", color="Country")
fig.show()


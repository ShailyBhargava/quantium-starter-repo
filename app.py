import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read the cleaned CSV
df = pd.read_csv("formatted_sales_data.csv")

# Convert date column to datetime type
df["date"] = pd.to_datetime(df["date"])

# Group by date and sum sales
daily_sales = df.groupby("date").sum().reset_index()

# Create Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualizer"

# Layout of the app
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Over Time", style={'textAlign': 'center'}),

    dcc.Graph(
        figure=px.line(
            daily_sales,
            x="date",
            y="sales",
            title="Daily Sales of Pink Morsels",
            labels={"date": "Date", "sales": "Total Sales"},
        )
    )
])

if __name__ == "__main__":
    app.run(debug=True)

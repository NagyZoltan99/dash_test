from dash import Dash, dcc, html
import plotly.graph_objects as go

# Create a Dash app
app = Dash(__name__)
server = app.server

# Create a simple Plotly graph
fig = go.Figure()

# Add a scatter plot
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17], mode='lines+markers', name='Line 1'))

# Add a bar plot
fig.add_trace(go.Bar(x=[1, 2, 3, 4], y=[5, 6, 7, 8], name='Bar 1'))

# Update layout
fig.update_layout(
    title="Simple Dash App Example",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    template="plotly_white",
)

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children="Hello Dash!", style={'textAlign': 'center'}),
    html.P("This is a simple Dash app with a Plotly graph.", style={'textAlign': 'center'}),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False)

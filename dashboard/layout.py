# dashboard/layout.py

from dash import html, dcc


def create_layout(year_list, dropdown_options):
    return html.Div([
        html.H1(
            "Automobile Sales Dashboard",
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}
        ),

        html.Div([
            html.Label("Select Statistics:"),
            dcc.Dropdown(
                id='select-statistics',
                options=dropdown_options,
                value='Yearly Statistics',
                placeholder='Select a report type'
            )
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div([
            html.Label("Select Year:"),
            dcc.Dropdown(
                id='select-year',
                options=[{'label': i, 'value': i} for i in year_list],
                value=2020
            )
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),

        html.Div(id='output-container', className='output-container', style={'padding': '10px'})
    ])

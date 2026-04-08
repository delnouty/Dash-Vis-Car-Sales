import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from data_loader import load_data
import config


def create_app(data_url: str) -> dash.Dash:
    data = load_data(data_url)

    app = dash.Dash(__name__)
    app.title = "Automobile Statistics Dashboard"

    # ---------- Layout ----------
    app.layout = html.Div([
        html.H1(
            "Automobile Sales Dashboard",
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}
        ),
        html.Div([
            html.Label("Select Statistics:"),
            dcc.Dropdown(
                id='select-statistics',
                options=config.DROPDOWN_OPTIONS,
                value='Yearly Statistics',
                placeholder='Select a report type'
            )
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([
            html.Label("Select Year:"),
            dcc.Dropdown(
                id='select-year',
                options=[{'label': i, 'value': i} for i in config.YEAR_LIST],
                value=2020
            )
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div(id='output-container', className='output-container', style={'padding': '10px'})
    ])

    # ---------- Callbacks ----------

    @app.callback(
        Output(component_id='select-year', component_property='disabled'),
        Input(component_id='select-statistics', component_property='value')
    )
    def update_input_container(selected_statistics):
        return selected_statistics != 'Yearly Statistics'

    @app.callback(
        Output(component_id='output-container', component_property='children'),
        [Input(component_id='select-statistics', component_property='value'),
         Input(component_id='select-year', component_property='value')]
    )
    def update_output_container(selected_statistics, input_year):
        if selected_statistics == 'Recession Period Statistics':
            recession_data = data[data['Recession'] == 1]
            recession_years = recession_data['Year'].unique()

            yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
            R_chart1 = dcc.Graph(
                figure=px.line(
                    yearly_rec,
                    x='Year',
                    y='Automobile_Sales',
                    title="Average Automobile Sales fluctuation over Recession Period"
                ).update_layout(xaxis=dict(tickvals=recession_years, tickangle=-90))
            )

            average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
            R_chart2 = dcc.Graph(
                figure=px.bar(
                    average_sales,
                    x='Vehicle_Type',
                    y='Automobile_Sales',
                    title='Average Number of Vehicles Sold by Vehicle Type during Recession Period',
                    color='Vehicle_Type',
                    color_discrete_map=config.COLOR_MAP
                ).update_layout(xaxis=dict(categoryorder='array',
                                           categoryarray=config.VEHICLE_TYPE_ORDER))
            )

            return html.Div([R_chart1, R_chart2])

        else:
            yearly_data = data[data['Year'] == input_year]

            # Plot 1: Yearly Automobile sales using line chart for the whole period
            yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
            Y_chart1 = dcc.Graph(
                figure=px.line(
                    yas,
                    x='Year',
                    y='Automobile_Sales',
                    title='Yearly Automobile Sales'
                )
            )

            # Plot 2: Total Monthly Automobile sales using line chart
            mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
            mas['Month'] = pd.Categorical(mas['Month'],
                                          categories=config.MONTH_ORDER,
                                          ordered=True)
            mas = mas.sort_values('Month')
            Y_chart2 = dcc.Graph(
                figure=px.line(
                    mas,
                    x='Month',
                    y='Automobile_Sales',
                    title='Total Monthly Automobile Sales'
                )
            )

            # Plot 3: Number of vehicles sold during the given year by vehicle type
            total_sales = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
            Y_chart3 = dcc.Graph(
                figure=px.bar(
                    total_sales,
                    x='Vehicle_Type',
                    y='Automobile_Sales',
                    title=f'Number of Vehicles Sold by Vehicle Type in {input_year}',
                    color='Vehicle_Type',
                    color_discrete_map=config.COLOR_MAP,
                    category_orders={'Vehicle_Type': config.VEHICLE_TYPE_ORDER}
                )
            )

            # Plot 4: Total Advertisement Expenditure for each vehicle type using pie chart
            exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
            Y_chart4 = dcc.Graph(
                figure=px.pie(
                    exp_data,
                    names='Vehicle_Type',
                    values='Advertising_Expenditure',
                    title=f'Total Advertisement Expenditure by Vehicle Type in {input_year}'
                )
            )
            Y_chart4.figure.update_traces(
                marker=dict(
                    colors=[config.COLOR_MAP.get(i, '#000000')
                            for i in exp_data['Vehicle_Type']]
                )
            )

            return html.Div([Y_chart1, Y_chart2, Y_chart3, Y_chart4])

    return app


if __name__ == '__main__':
    DATA_URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv'
    app = create_app(DATA_URL)
    app.run_server(debug=False)


# dashboard/callbacks.py

from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


def register_callbacks(app, data, color_map, month_order, vehicle_type_order):

    @app.callback(
        Output('select-year', 'disabled'),
        Input('select-statistics', 'value')
    )
    def update_input_container(selected_statistics):
        return selected_statistics != 'Yearly Statistics'

    @app.callback(
        Output('output-container', 'children'),
        [Input('select-statistics', 'value'),
         Input('select-year', 'value')]
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
                    color_discrete_map=color_map
                ).update_layout(xaxis=dict(categoryorder='array',
                                           categoryarray=vehicle_type_order))
            )

            return html.Div([R_chart1, R_chart2])

        else:
            yearly_data = data[data['Year'] == input_year]

            yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
            Y_chart1 = dcc.Graph(
                figure=px.line(
                    yas,
                    x='Year',
                    y='Automobile_Sales',
                    title='Yearly Automobile Sales'
                )
            )

            mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
            mas['Month'] = pd.Categorical(mas['Month'], categories=month_order, ordered=True)
            mas = mas.sort_values('Month')
            Y_chart2 = dcc.Graph(
                figure=px.line(
                    mas,
                    x='Month',
                    y='Automobile_Sales',
                    title='Total Monthly Automobile Sales'
                )
            )

            total_sales = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].sum().reset_index()
            Y_chart3 = dcc.Graph(
                figure=px.bar(
                    total_sales,
                    x='Vehicle_Type',
                    y='Automobile_Sales',
                    title=f'Number of Vehicles Sold by Vehicle Type in {input_year}',
                    color='Vehicle_Type',
                    color_discrete_map=color_map,
                    category_orders={'Vehicle_Type': vehicle_type_order}
                )
            )

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
                marker=dict(colors=[color_map.get(i, '#000000') for i in exp_data['Vehicle_Type']])
            )

            return html.Div([Y_chart1, Y_chart2, Y_chart3, Y_chart4])

# Вспомогательные функции для тестов (не используются Dash напрямую)

def _test_update_input_container(selected_statistics):
    return selected_statistics != 'Yearly Statistics'

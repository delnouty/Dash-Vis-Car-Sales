# dashboard/__init__.py

import dash

from .data_loader import load_data
from .layout import create_layout
from .callbacks import register_callbacks
from . import config


def create_app(data_url: str) -> dash.Dash:
    data = load_data(data_url)

    app = dash.Dash(__name__)
    app.title = "Automobile Statistics Dashboard"

    app.layout = create_layout(
        year_list=config.YEAR_LIST,
        dropdown_options=config.DROPDOWN_OPTIONS
    )

    register_callbacks(
        app=app,
        data=data,
        color_map=config.COLOR_MAP,
        month_order=config.MONTH_ORDER,
        vehicle_type_order=config.VEHICLE_TYPE_ORDER
    )

    return app

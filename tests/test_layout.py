# tests/test_layout.py

from dashboard.layout import create_layout
import dashboard.config as cfg
from dash import html


def test_layout_structure():
    layout = create_layout(cfg.YEAR_LIST, cfg.DROPDOWN_OPTIONS)

    # Проверяем, что layout — это html.Div
    assert isinstance(layout, html.Div)

    # Проверяем, что есть контейнер output-container
    # layout.children — это список элементов внутри Div
    ids = []

    for child in layout.children:
        # Некоторые элементы — Div, некоторые — H1, некоторые — другие компоненты
        if hasattr(child, "id") and child.id is not None:
            ids.append(child.id)

        # Внутренние Div тоже могут содержать id
        if hasattr(child, "children") and isinstance(child.children, list):
            for sub in child.children:
                if hasattr(sub, "id") and sub.id is not None:
                    ids.append(sub.id)

    assert "output-container" in ids

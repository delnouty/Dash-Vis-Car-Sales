# tests/test_callbacks.py

from dashboard.callbacks import _test_update_input_container


def test_update_input_container():
    assert _test_update_input_container("Yearly Statistics") is False
    assert _test_update_input_container("Recession Period Statistics") is True

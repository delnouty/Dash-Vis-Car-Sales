# tests/test_config.py

import dashboard.config as cfg


def test_config_constants():
    assert len(cfg.YEAR_LIST) > 0
    assert "Jan" in cfg.MONTH_ORDER
    assert isinstance(cfg.COLOR_MAP, dict)
    assert "Supperminicar" in cfg.COLOR_MAP

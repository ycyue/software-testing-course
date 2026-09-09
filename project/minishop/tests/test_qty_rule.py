from server import qty_allowed


def test_qty_one_allowed():
    assert qty_allowed(1, 10) is True


def test_qty_equals_stock():
    assert qty_allowed(10, 10) is True


def test_qty_over_stock():
    assert qty_allowed(11, 10) is False


def test_qty_wrong_type():
    assert qty_allowed("11", 10) is False

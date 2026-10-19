import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result", [
    (0, [0,0,0,0]),
    (1, [1,0,0,0]),
    (4, [4,0,0,0]),
    (5, [0,1,0,0]),
    (6, [1,1,0,0]),
    (9, [4,1,0,0]),
    (10, [0,0,1,0]),
    (11, [1,0,1,0]),
    (17, [2,1,1,0]),
    (24, [4,0,2,0]),
    (25, [0,0,0,1]),
    (33, [3,1,0,1]),
    (50, [0,0,0,2]),
    (99, [4,0,2,3]),
    (100, [0,0,0,4]),
    (509, [4,1,0,20]),
    (1024, [4,0,2,40]),
    (903, [3,0,0,36]),
    ]
)
def test_cents_get_coin_combination(cents, result):
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "input_error", [
    ("text"),
    (None),
    (["list"])
    ]
)
def test_type_errors_get_coin_combination(input_error):
    with pytest.raises(TypeError):
        get_coin_combination(input_error)

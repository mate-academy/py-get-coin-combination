import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    ("cents", "result"),
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="should return 1 penny"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should return nickels every 5 cents"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return dimes every 10 cents"),
        pytest.param(50, [0, 0, 0, 2],
                     id="should return quarter for every 25 cents"),
        pytest.param(56, [1, 1, 0, 2],
                     id="should return quarter for every 25 cents"),
    ]
)
def test_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

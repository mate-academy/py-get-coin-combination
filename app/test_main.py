import pytest
from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, expected_list",
    [
        pytest.param(0, [0, 0, 0, 0], id="when coins equals 0"),
        pytest.param(1, [1, 0, 0, 0], id="when coins equals 1 penny"),
        pytest.param(5, [0, 1, 0, 0], id="when coins equals 1 nickel"),
        pytest.param(10, [0, 0, 1, 0], id="when coins equals 1 dime"),
        pytest.param(25, [0, 0, 0, 1], id="when coins equals 1 quarter"),
    ]
)
def test_get_coin_base_combination(coin: int, expected_list: list) -> None:
    assert get_coin_combination(coin) == expected_list


@pytest.mark.parametrize(
    "coin, expected_list",
    [
        pytest.param(6, [1, 1, 0, 0],
                     id="when coins equals 1 nickel and 1 penny"),
        pytest.param(17, [2, 1, 1, 0],
                     id="when coins equals 2 pennies + 1 nickel + 1 dime"),
        pytest.param(30, [0, 1, 0, 1],
                     id="when coins equals 1 dime + 1 quarter"),
        pytest.param(50, [0, 0, 0, 2],
                     id="when coins equals 2 quarter"),
    ]
)
def test_get_coin_combination_with_other_number(coin: int,
                                                expected_list: list) -> None:
    assert get_coin_combination(coin) == expected_list


@pytest.mark.parametrize(
    "coin, expected_error",
    [
        pytest.param("1", TypeError, id="coins not str"),
        pytest.param(1.5, TypeError, id="coins not int"),
        pytest.param(-1, ValueError, id="coins is negative"),
    ]
)
def test_get_coin_errors(coin: Any, expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(coin)

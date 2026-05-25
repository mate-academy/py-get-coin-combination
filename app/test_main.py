from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test 1 penny + 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test 2 pennies + 1 nickel + 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test 2 quarters"
        ),
    ]
)
def test_get_coin_combination(value: int, expected: list[int]) -> None:
    assert get_coin_combination(value) == expected


@pytest.mark.parametrize(
    "value,expected_error",
    [
        pytest.param(
            "1",
            TypeError,
            id="test values  should be integer"
        ),
    ]
)
def test_errors(value: int, expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(value)

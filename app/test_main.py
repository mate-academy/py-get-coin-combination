import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),  # zero amount
        (1, [1, 0, 0, 0]),  # 1 penny
        (4, [4, 0, 0, 0]),  # pennies only
        (5, [0, 1, 0, 0]),  # 1 nickel
        (6, [1, 1, 0, 0]),  # example
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),  # 1 dime
        (17, [2, 1, 1, 0]),  # example
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),  # 1 quarter
        (26, [1, 0, 0, 1]),
        (50, [0, 0, 0, 2]),  # example
        (99, [4, 0, 2, 3]),  # boundary case
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_all_values_are_non_negative_integers() -> None:
    result = get_coin_combination(88)
    for value in result:
        assert isinstance(value, int)
        assert value >= 0


def test_return_type_and_length() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4

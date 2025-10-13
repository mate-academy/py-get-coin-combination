import pytest
from app.main import get_coin_combination

# main test checking basic combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),  # one penny expected
        (6, [1, 1, 0, 0]),  # one penny one nickel
        (17, [2, 1, 1, 0]),  # two pens one nickel one dime
        (50, [0, 0, 0, 2]),  # two quarters
        (0, [0, 0, 0, 0]),  # no coins
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    result = get_coin_combination(cents)
    assert result == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),

        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),

        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),

        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),

    ]
)
def test_get_coin_combination_boundaries(cents: int, expected: int) -> None:
    result = get_coin_combination(cents)
    assert result == expected


def test_get_coin_combination_returns_list_of_four_ints() -> None:
    result = get_coin_combination(49)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)


def test_get_coin_combination_zero_cents_returns_empty_combination() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0]


def test_get_coin_combination_big_value() -> None:
    result = get_coin_combination(9999)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "invalid_input",
    [
        -1,
        -100,
        2.5,
        "10",
        None,
        [1, 2],
        {"cents": 10},
        True,
    ]
)
def test_get_coin_combination_raises_error_for_invalid_input(
        invalid_input: str
) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(invalid_input)

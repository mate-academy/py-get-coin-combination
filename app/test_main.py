import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (14, [4, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
        (1000001, [1, 0, 0, 40000]),
    ],
)
def test_get_coin_combination_should_return_minimal_coins(
    cents: int, expected: list
) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_should_return_list_of_four_ints() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(coin, int) for coin in result)


@pytest.mark.parametrize("cents", ["10", None])
def test_get_coin_combination_should_raise_error_for_invalid_type(
    cents: object,
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

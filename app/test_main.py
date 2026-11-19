import pytest

from app import main


def test_not_string() -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination("100")


def test_float_input() -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination(1.5)


def test_negative_number() -> None:
    with pytest.raises(ValueError):
        main.get_coin_combination(-1)


@pytest.mark.parametrize(
    "coins, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_return_correct_coin_combination(coins: int, expected: list) -> None:
    assert main.get_coin_combination(coins) == expected


@pytest.mark.parametrize(
    "coins, expected",
    [
        (30, [0, 1, 0, 1]),
        (41, [1, 1, 1, 1]),

    ]
)
def test_return_different_coins_not_only_pennies(
        coins: int,
        expected: list
) -> None:
    assert main.get_coin_combination(coins) == expected


@pytest.mark.parametrize(
    "coins, expected",
    [
        (7, [2, 1, 0, 0]),
        (50, [0, 0, 0, 2]),
        (11, [1, 0, 1, 0])

    ]
)
def test_return_coins_of_different_types(coins: int, expected: list) -> None:
    assert main.get_coin_combination(coins) == expected

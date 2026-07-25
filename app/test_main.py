import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_examples(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_structure() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)
    assert all(x >= 0 for x in result)


def test_minimal_coins() -> None:
    cents = 41
    coins = get_coin_combination(cents)
    total = sum(coins)

    min_possible = float("inf")
    for pennies in range(0, cents + 1):
        for nickels in range(0, cents // 5 + 1):
            for dimes in range(0, cents // 10 + 1):
                for quarters in range(0, cents // 25 + 1):
                    if (
                            pennies + 5 * nickels
                            + 10 * dimes
                            + 25 * quarters == cents
                    ):
                        min_possible = min(
                            min_possible,
                            pennies + nickels
                            + dimes + quarters
                        )
    assert total == min_possible


def test_large() -> None:
    coins = get_coin_combination(999)
    assert coins[3] == 999 // 25

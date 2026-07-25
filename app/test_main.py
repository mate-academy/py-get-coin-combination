import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (4, [4, 0, 0, 0])
    ]
)
def test_should_return_penies_when_cents_less_five(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result, (
        "Function should return penies when cents less five"
    )


@pytest.mark.parametrize(
    "cents,result",
    [
        (6, [1, 1, 0, 0]),
        (7, [2, 1, 0, 0]),
        (8, [3, 1, 0, 0]),
        (9, [4, 1, 0, 0])
    ]
)
def test_should_return_penies_and_nickels(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result, (
        "Function should return penies and nickels"
    )


@pytest.mark.parametrize(
    "cents,result",
    [
        (11, [1, 0, 1, 0]),
        (13, [3, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (17, [2, 1, 1, 0])
    ]
)
def test_should_return_penies_and_nickels_and_dimes(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result, (
        "Function should return penies and nickels and dimes"
    )


@pytest.mark.parametrize(
    "cents,result",
    [
        (26, [1, 0, 0, 1]),
        (27, [2, 0, 0, 1]),
        (37, [2, 0, 1, 1]),
        (57, [2, 1, 0, 2]),
    ]
)
def test_should_return_penies_and_nickels_and_dimes_and_quaters(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result, (
        "Function should return penies and nickels and dimes and quaters"
    )


@pytest.mark.parametrize(
    "cents,result",
    [
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (25, [0, 0, 0, 1])
    ]
)
def test_should_return_coins_when_cents_are_divisiable(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result, (
        "Function should return coins when cents are divisiable"
    )

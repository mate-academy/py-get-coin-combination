import pytest

from typing import Type

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]

)
def test_return_coin_combination(coin: int, result: list) -> None:
    assert (get_coin_combination(coin)) == result


def test_length_return_coin_combination() -> None:
    assert len(get_coin_combination(0)) == 4


@pytest.mark.parametrize(
    "coin, typeerror",
    [
        ("25", TypeError),
        ([15], TypeError),
        ({25: 15}, TypeError),
    ]
)
def test_coin_combination_integer(
        coin: int,
        typeerror: Type[Exception]
) -> None:
    with pytest.raises(typeerror):
        get_coin_combination(coin)

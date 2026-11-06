from app.main import get_coin_combination
import pytest


def test_cents_should_be_positive_number() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


@pytest.mark.parametrize(
    "coin",
    [
        ("15"),
        (None),
        ([15]),
        (15.5),
        (True)
    ]
)
def test_cents_incorrect_type_rises_type_error(coin: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(coin)


def test_cents_0_should_return_list_with_four_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "coin,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (98, [3, 0, 2, 3])
    ]
)
def test_get_coin_combination(coin: int, result: list) -> None:
    assert get_coin_combination(coin) == result

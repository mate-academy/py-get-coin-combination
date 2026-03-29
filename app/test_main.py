from app.main import get_coin_combination
import pytest

@pytest.mark.parametrize(
    "coin, expected",
    [
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 2, 0, 0]),
        (24, [4, 2, 0, 0]),
        (25, [0, 0, 1, 0]),
        (49, [4, 0, 2, 1]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_coin_combination(coin: int, expected: list[int]) -> None:
    assert get_coin_combination(coin) == expected

@pytest.mark.parametrize(
    "coin",
    [
        (-1),
        (-5),
        (-10),
        (-25),
    ],
)
def test_negative_ages(coin: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(coin)

@pytest.mark.parametrize(
    "coin",
    [
        ("a"),
        (None),
        ([1]),
        ({"dog": 3}),
    ],
)
def test_invalid_types(coin: object) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(coin)
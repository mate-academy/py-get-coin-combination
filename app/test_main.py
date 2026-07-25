import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (67, [2, 1, 1, 2]),
        (124, [4, 0, 2, 4]),
    ],
    ids=["Cents are zero",
         "One cent",
         "Six cents",
         "Seventeen cents",
         "Fifty cents",
         "Sixty-seven cents",
         "One hundred twenty-four cents"]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("cents")

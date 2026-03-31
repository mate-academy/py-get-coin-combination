import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_data",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (999, [4, 0, 2, 39])
    ]
)
def test_get_coin_combination_with_correct_data(
        cents: int, expected_data: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_data


@pytest.mark.parametrize(
    "cents",
    [
        (None,),
        ("5",),
        ("five",)
    ]
)
def test_get_coin_combination_with_invalid_data(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

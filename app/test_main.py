import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination_various_amounts(cents: int,
                                              expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_result_length() -> None:
    assert len(get_coin_combination(100)) == 4


def test_get_coin_combination_raises_error_on_invalid_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("10")

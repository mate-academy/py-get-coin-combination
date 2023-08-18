from typing import Any
import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, coin_combinations",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (42, [2, 1, 1, 1]),
        (10, [0, 0, 1, 0]),
        (100, [0, 0, 0, 4])
    ]
)
def test_different_coin_combinations(cent: int,
                                     coin_combinations: list) -> None:

    assert get_coin_combination(cent) == coin_combinations


@pytest.mark.parametrize(
    "cent, error",
    [
        (None, TypeError),
        ("1", TypeError)
    ]
)
def test_should_raise_correct_errors(cent: int,
                                     error: Any) -> None:

    with pytest.raises(error):
        get_coin_combination(cent)

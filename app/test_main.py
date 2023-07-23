import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "func, expected",
    [
        (len(get_coin_combination(1)), 4),
        (get_coin_combination(1), [1, 0, 0, 0]),
        (get_coin_combination(6), [1, 1, 0, 0]),
        (get_coin_combination(17), [2, 1, 1, 0]),
        (get_coin_combination(50), [0, 0, 0, 2]),
    ]
)
def test_coin_combination(func: int | list,
                          expected: list | int) -> None:
    assert func == expected

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("coins, expected",
                         [
                             (0, [0, 0, 0, 0]),
                             (1, [1, 0, 0, 0]),
                             (5, [0, 1, 0, 0]),
                             (10, [0, 0, 1, 0]),
                             (25, [0, 0, 0, 1]),
                             (6, [1, 1, 0, 0]),
                             (17, [2, 1, 1, 0]),
                             (30, [0, 1, 0, 1]),
                             (50, [0, 0, 0, 2]),
                             (99, [4, 0, 2, 3]),
                         ],
                         )
def test_simple_coin_combination(
        coins: int,
        expected: list,
) -> None:
    assert get_coin_combination(coins) == expected


def test_valid_len_list() -> None:
    assert len(get_coin_combination(1000)) == 4

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (1_000_049, [4, 0, 2, 40_001])
    ]
)
def test_get_human_age(cents: int,
                        expected_list: list[int]) -> None:
    assert get_coin_combination(cents) == expected_list

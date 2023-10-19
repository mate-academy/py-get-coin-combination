import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coin_combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_return_coin_combination_list(cents: int,
                                      expected_coin_combination: list) -> None:
    assert get_coin_combination(cents) == expected_coin_combination

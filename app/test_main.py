import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4])
    ]
)
def test_should_return_correct_combination(
        cents: int, expected_list: list) -> None:
    assert get_coin_combination(cents) == expected_list

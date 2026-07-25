import pytest
from app.main import get_coin_combination


def test_should_return_list() -> None:
    assert isinstance(get_coin_combination(1), list)


def test_should_return_correct_length() -> None:
    assert len(get_coin_combination(1)) == 4


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_coin_combination_results(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

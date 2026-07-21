import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, list_expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (55, [0, 1, 0, 2]),
        (76, [1, 0, 0, 3]),
        (156, [1, 1, 0, 6]),
    ],
)
def test_should_to_return_correct_list(
        cents: int,
        list_expected: list
) -> None:
    assert get_coin_combination(cents) == list_expected

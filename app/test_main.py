import pytest

from app.main import get_coin_combination


def test_should_return_list_of_given_length():
    assert len(get_coin_combination(1)) == 4


@pytest.mark.parametrize(
    "cents, expected_result", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_return_get_coin_combination(cents, expected_result):
    assert get_coin_combination(cents) == expected_result

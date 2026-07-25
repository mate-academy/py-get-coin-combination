from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_data",
    [
        (
            1,
            [1, 0, 0, 0]
        ),
        (
            6,
            [1, 1, 0, 0]
        ),
        (
            17,
            [2, 1, 1, 0]
        ),
        (
            50,
            [0, 0, 0, 2]
        ),
        (
            999,
            [4, 0, 2, 39]
        ),
    ]
)
def test_check_data_correctly(cents : int,
                              expected_data: list) -> None:
    assert get_coin_combination(cents) == expected_data

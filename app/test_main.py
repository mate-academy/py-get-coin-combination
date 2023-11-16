import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected",
                         [
                             (0, [0, 0, 0, 0]),
                             (1, [1, 0, 0, 0]),
                             (5, [0, 1, 0, 0]),
                             (6, [1, 1, 0, 0]),
                             (13, [3, 0, 1, 0]),
                             (16, [1, 1, 1, 0]),
                             (17, [2, 1, 1, 0]),
                             (20, [0, 0, 2, 0]),
                             (25, [0, 0, 0, 1]),
                             (30, [0, 1, 0, 1]),
                             (50, [0, 0, 0, 2]),
                             (101, [1, 0, 0, 4]),
                             (994, [4, 1, 1, 39]),
                             (999, [4, 0, 2, 39])
                         ]
                         )
def test_should_return_expected_results(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

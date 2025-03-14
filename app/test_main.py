import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (0, [0, 0, 0, 0]),
    ]
)


def test_coin_combination(cents, expected_result):
    res = get_coin_combination(cents)
    assert res == expected_result

import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (57, [2, 1, 0, 2])
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        ("21", TypeError),
        ([32], TypeError)
    ]
)
def test_get_coin_combination_for_error(
        cents: int,
        expected_error: Exception
) -> None:
    with pytest.raises(Exception):
        get_coin_combination(cents)

import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (0, [0, 0, 0, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
        (99, [4, 0, 2, 3]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

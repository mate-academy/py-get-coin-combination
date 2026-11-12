import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(amount: int, expected: list[int]) -> None:
    assert get_coin_combination(amount) == expected

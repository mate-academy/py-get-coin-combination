import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number, result",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (99, [4, 0, 2, 3]),
        (1000, [0, 0, 0, 40])
    ]
)
def test_get_coin_combination(number: int, result: list) -> None:
    assert get_coin_combination(number) == result

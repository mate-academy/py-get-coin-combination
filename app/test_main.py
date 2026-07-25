import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize("coin, expected", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (25, [0, 0, 0, 1]),
    (77, [2, 0, 0, 3]),
    (1000000, [0, 0, 0, 40000]),
],)
def test_get_coin_combination(coin: int, expected: list) -> None:
    assert get_coin_combination(coin) == expected, (
        f"Function 'coin_combination' should return {coin} "
        f"when value is {expected}"
    )

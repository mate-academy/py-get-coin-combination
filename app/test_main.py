from app.main import get_coin_combination


# write your tes
import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),     # немає монет
        (1, [1, 0, 0, 0]),     # 1 пенні
        (5, [0, 1, 0, 0]),     # 1 нікель
        (10, [0, 0, 1, 0]),    # 1 дайм
        (25, [0, 0, 0, 1]),    # 1 чверть
        (6, [1, 1, 0, 0]),     # 1 пенні + 1 нікель
        (17, [2, 1, 1, 0]),    # 2 пенні + 1 нікель + 1 дайм
        (50, [0, 0, 0, 2]),    # 2 quarters
        (99, [4, 0, 2, 3]),    # 99 = 3×25 + 2×10 + 4×1
    ]
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


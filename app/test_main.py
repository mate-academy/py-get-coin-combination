import pytest
from app.main import get_coin_combination

@pytest.mark.parametrize(
    "cents, expected",
    [
        # Граничний випадок (0 центів)
        (0, [0, 0, 0, 0]),
        
        # Базові приклади з умови завдання
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        
        # Точні номінали окремих монет
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        
        # Інші комбінації для повної перевірки логіки
        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (14, [4, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (43, [3, 1, 1, 1]),
        (99, [4, 0, 2, 3]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

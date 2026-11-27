import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    ("cents", "expected"),
    [
        # Граничний випадок: 0 центів
        (0, [0, 0, 0, 0]),
        # Пенні (1 цент) та межа перед нікелем
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        # Нікель (5 центів) та комбінації з пенні
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        # Дайм (10 центів) та проміжні значення
        (10, [0, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        # Квотер (25 центів) та більші суми
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


def test_return_type_and_length() -> None:
    result = get_coin_combination(42)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(count, int) and count >= 0 for count in result)

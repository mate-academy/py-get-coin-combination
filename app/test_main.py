import pytest
from app import main


# Тести для різних значень суми в центрах
@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (30, [0, 1, 0, 1]),
        (100, [0, 0, 0, 4]),
        (3, [3, 0, 0, 0]),
        (21, [1, 0, 2, 0]),
        (42, [2, 1, 1, 1]),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    """
    Тестує функцію get_coin_combination, що повертає найменшу кількість монет
    для заданої кількості центів.

    Параметри:
    - cents (int): кількість центів.
    - expected (list): очікуваний результат у вигляді списку монет.
    """
    result = main.get_coin_combination(cents)
    assert result == expected, (f"Помилка при cents={cents}, "
                                f"отримано {result}")


# Тест для граничного випадку: 0 центів
def test_zero_cents() -> None:
    """
    Перевіряє випадок, коли кількість центів дорівнює 0.
    Ожидаемый результат - [0, 0, 0, 0], оскільки немає монет.
    """
    result = main.get_coin_combination(0)
    assert result == [0, 0, 0, 0], f"Помилка при 0 центів, отримано {result}"


# Тест для великого значення
@pytest.mark.parametrize(
    "cents, expected",
    [
        (1000, [0, 0, 0, 40]),
        (12345, [0, 0, 2, 493]),
    ],
)
def test_large_values(cents: int, expected: list) -> None:
    """
    Перевіряє функцію для великих значень суми.
    """
    result = main.get_coin_combination(cents)
    assert result == expected, (f"Помилка при cents={cents}, "
                                f"отримано {result}")

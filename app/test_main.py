from app.main import get_coin_combination


def test_zero_cents() -> None:
    """Проверяет, что для 0 центов возвращается нулевая комбинация."""
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_penny() -> None:
    """Проверяет минимальную сумму в 1 цент."""
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_combination_with_nickel() -> None:
    """Проверяет комбинацию с nickel (5 центов)."""
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]  # 5¢ + 1¢


def test_combination_with_dime() -> None:
    """Проверяет комбинацию с dime (10 центов)."""
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]  # 10¢ + 5¢ + 2¢


def test_combination_with_quarter() -> None:
    """Проверяет комбинацию с quarter (25 центов)."""
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]  # 25¢ × 2


def test_mixed_combination() -> None:
    """Проверяет комбинацию с несколькими типами монет."""
    assert get_coin_combination(41) == [1, 1, 1, 1]  # 25¢ + 10¢ + 5¢ + 1¢
    assert get_coin_combination(67) == [2, 1, 1, 2]  # 25¢ × 2 + 10¢ + 5¢ + 2¢


def test_sum_matches_cents() -> None:
    """Проверяет, что сумма монет равна исходному количеству центов."""
    assert sum([1 * 1, 5 * 0, 10 * 0, 25 * 0]) == 1  # Для 1
    assert sum([1 * 1, 5 * 1, 10 * 0, 25 * 0]) == 6  # Для 6
    assert sum([1 * 2, 5 * 1, 10 * 1, 25 * 0]) == 17  # Для 17
    assert sum([1 * 0, 5 * 0, 10 * 0, 25 * 2]) == 50  # Для 50

from app.main import get_coin_combination


def test_coin_combination_with_1_cent() -> None:
    result = get_coin_combination(1)
    assert result == [1, 0, 0, 0], f"Expected [1, 0, 0, 0] but got {result}"


def test_coin_combination_with_6_cents() -> None:
    result = get_coin_combination(6)
    assert result == [1, 1, 0, 0], f"Expected [1, 1, 0, 0] but got {result}"


def test_coin_combination_with_17_cents() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0], f"Expected [2, 1, 1, 0] but got {result}"


def test_coin_combination_with_50_cents() -> None:
    result = get_coin_combination(50)
    assert result == [0, 0, 0, 2], f"Expected [0, 0, 0, 2] but got {result}"


def test_coin_combination_with_0_cents() -> None:
    result = get_coin_combination(0)
    assert result == [0, 0, 0, 0], f"Expected [0, 0, 0, 0] but got {result}"


def test_coin_combination_with_large_amount() -> None:
    result = get_coin_combination(126)
    assert result == [1, 0, 0, 5], f"Expected [1, 0, 0, 5] but got {result}"

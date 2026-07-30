from app import main


def test_returns_zero_coins_for_zero_cents() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_returns_single_coin_types() -> None:
    assert main.get_coin_combination(1) == [1, 0, 0, 0]
    assert main.get_coin_combination(5) == [0, 1, 0, 0]
    assert main.get_coin_combination(10) == [0, 0, 1, 0]
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_returns_mixed_coin_combination() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]
    assert main.get_coin_combination(41) == [1, 1, 1, 1]
    assert main.get_coin_combination(99) == [4, 0, 2, 3]

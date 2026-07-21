from app.main import get_coin_combination


def test_get_coin_combination_only_pennies() -> None:
    assert (get_coin_combination(4) == [4, 0, 0, 0])
    assert (get_coin_combination(5) == [0, 1, 0, 0])
    assert (get_coin_combination(20) == [0, 0, 2, 0])
    assert (get_coin_combination(200) == [0, 0, 0, 8])


def test_get_coin_combination_all_types() -> None:
    assert (get_coin_combination(69) == [4, 1, 1, 2])

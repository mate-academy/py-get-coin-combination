from app.main import get_coin_combination

def test_get_coin_combination_1_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]

def test_get_coin_combination_1_penny_and_1_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]

def test_get_coin_combination_2_penny_and_1_nickel_and_1_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]

def test_get_coin_combination_2_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]

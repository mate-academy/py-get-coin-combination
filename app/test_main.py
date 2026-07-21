from app.main import get_coin_combination


def test_without_used_coins() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_coin() -> None:
    used_coins = get_coin_combination(1)
    assert used_coins[0] > 0
    assert used_coins[1] == 0
    assert used_coins[2] == 0
    assert used_coins[3] == 0


def test_one_penny_one_nickel() -> None:
    used_coins = get_coin_combination(6)
    assert used_coins[0] > 0
    assert used_coins[1] > 0
    assert used_coins[2] == 0
    assert used_coins[3] == 0


def test_1_pennies_1_nickel_1_dime() -> None:
    used_coins = get_coin_combination(16)
    assert used_coins[0] > 0
    assert used_coins[1] > 0
    assert used_coins[2] > 0
    assert used_coins[3] == 0


def test_1_pennies_1_nickel_1_dime_1_quarter() -> None:
    used_coins = get_coin_combination(41)
    assert used_coins[0] > 0
    assert used_coins[1] > 0
    assert used_coins[2] > 0
    assert used_coins[3] > 0

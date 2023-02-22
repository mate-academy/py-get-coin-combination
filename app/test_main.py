from app.main import get_coin_combination


def test_returns_correct_change() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_returns_list_of_length_4() -> None:
    assert len(get_coin_combination(0)) == 4
    assert len(get_coin_combination(1)) == 4
    assert len(get_coin_combination(100)) == 4


def test_returns_only_non_negative_integers() -> None:
    for i in range(100):
        coins = get_coin_combination(i)
        assert all(isinstance(c, int) and c >= 0 for c in coins)


def test_returns_smallest_combination() -> None:
    assert get_coin_combination(16) == [1, 1, 1, 0]
    assert get_coin_combination(12) == [2, 0, 1, 0]
    assert get_coin_combination(19) == [4, 1, 1, 0]
    assert get_coin_combination(26) == [1, 0, 0, 1]


def test_returns_coins_of_different_denominations() -> None:
    assert sum(get_coin_combination(99)) == 99


def test_returns_coins_of_different_types() -> None:
    coins = get_coin_combination(99)
    assert coins[0] > 0 or coins[1] > 0 or coins[2] > 0 or coins[3] > 0

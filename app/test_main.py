from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0], "Failed for 0 cents"

    assert get_coin_combination(1) == [1, 0, 0, 0], "Failed for 1 cent"
    assert get_coin_combination(4) == [4, 0, 0, 0], "Failed for 4 cents"

    assert get_coin_combination(5) == [0, 1, 0, 0], "Failed for 5 cents"
    assert get_coin_combination(6) == [1, 1, 0, 0], "Failed for 6 cents"

    assert get_coin_combination(10) == [0, 0, 1, 0], "Failed for 10 cents"
    assert get_coin_combination(17) == [2, 1, 1, 0], "Failed for 17 cents"

    assert get_coin_combination(25) == [0, 0, 0, 1], "Failed for 25 cents"
    assert get_coin_combination(50) == [0, 0, 0, 2], "Failed for 50 cents"

    assert get_coin_combination(41) == [1, 1, 1, 1], "Failed for 41 cents"
    assert get_coin_combination(99) == [4, 0, 2, 3], "Failed for 99 cents"

    assert get_coin_combination(100) == [0, 0, 0, 4], "Failed for 100 cents"
    assert get_coin_combination(123) == [3, 0, 2, 4], "Failed for 123 cents"

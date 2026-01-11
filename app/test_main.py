from app.main import get_coin_combination


# write your tests here
def test_get_coin_combination() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], "Test case 1 failed"
    assert get_coin_combination(6) == [1, 1, 0, 0], "Test case 2 failed"
    assert get_coin_combination(17) == [2, 1, 1, 0], "Test case 3 failed"
    assert get_coin_combination(50) == [0, 0, 0, 2], "Test case 4 failed"
    assert get_coin_combination(0) == [0, 0, 0, 0], "Test case 5 failed"
    assert get_coin_combination(99) == [4, 0, 2, 3], "Test case 6 failed"
    assert get_coin_combination(41) == [1, 1, 1, 1], "Test case 7 failed"
    assert get_coin_combination(100) == [0, 0, 0, 4], "Test case 8 failed"

from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], \
        "Test failed for input: 1"
    assert get_coin_combination(6) == [1, 1, 0, 0], \
        "Test failed for input: 6"
    assert get_coin_combination(17) == [2, 1, 1, 0], \
        "Test failed for input: 17"
    assert get_coin_combination(50) == [0, 0, 0, 2], \
        "Test failed for input: 50"
    assert get_coin_combination(41) == [1, 1, 1, 1], \
        "Test failed for input: 41"
    assert get_coin_combination(100) == [0, 0, 0, 4], \
        "Test failed for input: 100"

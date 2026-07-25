from app.main import get_coin_combination


def test_get_coin_combination_should_return_correct_combination() -> None:

    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(36) == [1, 0, 1, 1]
    assert get_coin_combination(99) == [4, 0, 2, 3]
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert len(set(get_coin_combination(36))) == 2

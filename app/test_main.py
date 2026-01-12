from app.main import get_coin_combination


def test_should_return_expected_list_of_numbers() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(0) == [0, 0, 0, 0]

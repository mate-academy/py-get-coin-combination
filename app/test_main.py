from app.main import get_coin_combination


def test_should_return_different_types_of_coins() -> None:
    assert get_coin_combination(44) == [4, 1, 1, 1]


def test_should_return_list() -> None:
    assert get_coin_combination(44) == [4, 1, 1, 1]


def test_should_return_same_amount() -> None:
    values = [1, 5, 10, 25]
    result = get_coin_combination(10)
    cents = 0
    for index in range(4):
        cents += values[index] * result[index]
    assert cents == 10


def test_return_smallest_possible_number_of_coins() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_return_empty_list_when_cents_is_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]

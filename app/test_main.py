from app.main import get_coin_combination

def test_return_list() -> None:
    assert type(get_coin_combination(0)) is list


def test_should_return_4_zero_list_if_cents_0() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_coin_result() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_multiple_coin_result() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]
    assert get_coin_combination(15) == [0, 1, 1, 0]
    assert get_coin_combination(34) == [4, 1, 0, 1]

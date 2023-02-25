from app.main import get_coin_combination


def test_should_return_zero_when_cents_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_array_len_four() -> None:
    assert len(get_coin_combination(1)) == 4


def test_number_one() -> None:
    assert get_coin_combination(42) == [2, 1, 1, 1]

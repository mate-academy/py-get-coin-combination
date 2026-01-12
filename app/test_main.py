from app.main import get_coin_combination


def test_should_return_correct_result_if_cents_are_positive():
    cents = 15
    assert get_coin_combination(cents) == [0, 1, 1, 0]


def test_should_return_zeros_if_cents_are_equal_to_zero():
    cents = 0
    assert get_coin_combination(cents) == [0, 0, 0, 0]


def test_should_return_correct_result_with_big_amount():
    cents = 1347
    assert get_coin_combination(cents) == [2, 0, 2, 53]


def test_should_raise_error_if_cents_are_negative():
    cents = -12
    try:
        assert cents > 0
    except AssertionError:
        print("Cents must be bigger than 0!")


def test_cents_should_be_integers():
    cents = 14.7
    try:
        assert isinstance(cents, int)
    except AssertionError:
        print("Cents must be integers!")

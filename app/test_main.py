from app.main import get_coin_combination


def test_should_return_true_if_cents_type_equal_int():
    value = 0
    answer = True
    try:
        result = isinstance(get_coin_combination(value), int)
        assert answer == result
    except TypeError:
        assert answer is False


def test_should_return_0_if_cents_is_0():
    result = get_coin_combination(0)

    assert result == [0, 0, 0, 0]


def test_should_return_correct_number_of_pennies():
    result = get_coin_combination(4)

    assert result == [4, 0, 0, 0]


def test_should_return_correct_number_of_nickels():
    result = get_coin_combination(5)

    assert result == [0, 1, 0, 0]


def test_should_return_correct_number_of_dimes():
    result = get_coin_combination(10)

    assert result == [0, 0, 1, 0]


def test_should_return_correct_number_of_quarters():
    result = get_coin_combination(25)

    assert result == [0, 0, 0, 1]


def test_should_return_correct_amount_of_given_cents():
    result = get_coin_combination(94)

    assert result == [4, 1, 1, 3]

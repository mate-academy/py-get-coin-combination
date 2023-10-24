from app.main import get_coin_combination


def test_should_return_penny() -> None:
    cents = 1

    result = get_coin_combination(cents)

    assert result == [1, 0, 0, 0]


def test_should_return_nickel() -> None:
    cents = 6

    result = get_coin_combination(cents)

    assert result == [1, 1, 0, 0]


def test_should_return_dime() -> None:
    cents = 17

    result = get_coin_combination(cents)

    assert result == [2, 1, 1, 0]


def test_should_return_quarters() -> None:
    cents = 50

    result = get_coin_combination(cents)

    assert result == [0, 0, 0, 2]

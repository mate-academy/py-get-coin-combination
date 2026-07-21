from app.main import get_coin_combination


def test_checking_the_addition_penny() -> None:
    assert (
        get_coin_combination(1) == [1, 0, 0, 0]
    )


def test_checking_the_addition_nickel() -> None:
    assert (
        get_coin_combination(6) == [1, 1, 0, 0]
    )


def test_checking_the_addition_dime() -> None:
    assert (
        get_coin_combination(16) == [1, 1, 1, 0]
    )


def test_checking_the_addition_quarter() -> None:
    assert (
        get_coin_combination(41) == [1, 1, 1, 1]
    )

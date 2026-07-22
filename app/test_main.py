from app.main import get_coin_combination


def test_return_should_list_of_zeros_when_cents_equal_0() -> None:
    assert (
        get_coin_combination(0) == [0, 0, 0, 0]
    )


def test_should_return_the_smallest_possible_num_of_coins() -> None:
    assert (
        get_coin_combination(116) == [1, 1, 1, 4]
    )


def test_should_return_only_pennies_if_cents_lt_5() -> None:
    assert (
        get_coin_combination(4) == [4, 0, 0, 0]
    )

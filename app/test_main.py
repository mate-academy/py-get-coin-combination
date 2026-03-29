from app.main import get_coin_combination


def test_0_pennies() -> None:
    assert (get_coin_combination(0) == [0, 0, 0, 0]), (
        "Result should be equal to [0, 0, 0, 0]"
    )


def test_1_cents_is_a_pennies_on_1_position() -> None:
    assert (get_coin_combination(1) == [1, 0, 0, 0]), (
        "Result should be equal to [1, 0, 0, 0]"
    )


def test_5_cents_is_a_nickels_on_2_position() -> None:
    assert (get_coin_combination(5) == [0, 1, 0, 0]), (
        "Result should be equal to [0, 1, 0, 0]"
    )


def test_10_cents_is_a_dime_on_3_position() -> None:
    assert (get_coin_combination(20) == [0, 0, 2, 0]), (
        "Result should be equal to [0, 0, 2, 0]"
    )


def test_25_cents_is_a_quarter_on_4_position() -> None:
    assert (get_coin_combination(75) == [0, 0, 0, 3]), (
        "Result should be equal to [0, 0, 0, 3]"
    )


def test_use_all_coin_position() -> None:
    assert (get_coin_combination(41) == [1, 1, 1, 1]), (
        "Result should be equal to [1, 1, 1, 1]"
    )

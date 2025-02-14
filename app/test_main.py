from app.main import get_coin_combination


def test_should_return_the_same_value() -> None:
    assert get_coin_combination(17)[0] + \
           get_coin_combination(17)[1] * 5 + \
           get_coin_combination(17)[2] * 10 + \
           get_coin_combination(17)[3] * 25 == 17, \
           "Sum of returned combination should " \
           "be equal to passed value"


def test_combination_has_4_positions() -> None:
    assert len(get_coin_combination(4)) == 4, \
        "Should return a combination of four coins"


def test_returns_all_zeros_for_0_cents() -> None:
    assert set(get_coin_combination(0)) == {0}, \
        "Should return zeros for 0 cents"


def test_result_values_for_large_vals() -> None:
    assert get_coin_combination(22577) == [2, 0, 0, 903], \
        "Should return [2, 0, 0, 903] for 22577"


def test_returned_coins_number_is_the_smallest() -> None:
    assert get_coin_combination(22577)[0] < 5 and \
        get_coin_combination(22577)[1] < 2 and \
        get_coin_combination(22577)[2] < 3

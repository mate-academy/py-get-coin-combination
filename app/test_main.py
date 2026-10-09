from app.main import get_coin_combination


def test_should_return_zeros_when_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_should_return_only_pennies_when_cents_less_than_five() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_should_use_nickel_when_cents_from_five_to_nine() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_should_use_dimes_when_cents_from_ten_to_twenty_four() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]
    assert get_coin_combination(15) == [0, 1, 1, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(20) == [0, 0, 2, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_should_use_quarters_when_cents_is_25_or_more() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]
    assert get_coin_combination(26) == [1, 0, 0, 1]
    assert get_coin_combination(35) == [0, 0, 1, 1]
    assert get_coin_combination(50) == [0, 0, 0, 2]
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_should_return_list_of_four_elements_for_any_cents() -> None:
    for cents in range(201):
        assert len(get_coin_combination(cents)) == 4


def test_sum_of_coins_should_be_equal_to_cents_for_any_cents() -> None:
    for cents in range(201):
        pennies, nickels, dimes, quarters = get_coin_combination(cents)
        total = pennies + 5 * nickels + 10 * dimes + 25 * quarters
        assert total == cents


def test_should_use_smallest_number_of_coins_for_any_cents() -> None:
    for cents in range(201):
        pennies, nickels, dimes, quarters = get_coin_combination(cents)
        assert pennies < 5
        assert nickels < 2
        assert dimes < 3
        assert pennies + 5 * nickels + 10 * dimes < 25

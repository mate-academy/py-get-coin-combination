from app.main import get_coin_combination


def test_result_should_contain_quarters_when_cents_more_24() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_result_should_contain_dime_when_cents_more_9_and_less_25() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_result_should_contain_nickel_when_cents_more_4_and_less_10() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_result_should_contain_only_penny_when_cents_less_5() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_result_should_zeros_when_cents_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]

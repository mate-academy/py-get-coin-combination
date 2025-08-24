from app.main import get_coin_combination


def test_zero_cents_returns_empty_list() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_seventeen_cents_returns_expected_combination() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents_returns_two_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_ninety_nine_cents_returns_expected_combination() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]

def test_zero_cents_returns_empty_list() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_large_amount_returns_expected_combination() -> None:
    assert get_coin_combination(1499) == [4, 0, 2, 59]


def test_exact_quarter_returns_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]

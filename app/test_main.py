from app.main import get_coin_combination


def test_get_coin_combination_if_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination_if_cents_is_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_get_coin_combination_if_cents_is_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_get_coin_combination_if_cents_is_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_get_coin_combination_if_cents_is_twentyfive_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_get_coin_combination_if_cents_is_boundary_five_cents() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_get_coin_combination_if_cents_is_boundary_ten_cents() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_get_coin_combination_if_cents_is_boundary_twentyfive_cents() -> None:
    assert get_coin_combination(24) == [4, 0, 2, 0]


def test_get_coin_combination_if_cents_is_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_get_coin_combination_if_cents_is_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_get_coin_combination_if_cents_is_fourtyone_cents() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_get_coin_combination_if_cents_is_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]

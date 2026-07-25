from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_single_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_nickel_exact() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_dime_exact() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_quarter_exact() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_given_example_6() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_given_example_17() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_given_example_50() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_complex_case() -> None:
    assert get_coin_combination(87) == [2, 0, 1, 3]

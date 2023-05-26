from app.main import get_coin_combination


def test_should_return_1() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_1_1() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_three_elements() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_last() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_should_return_different_type() -> None:
    assert get_coin_combination(169) == [4, 1, 1, 6]


def test_should_return_different() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_should_return_different_r() -> None:
    assert get_coin_combination(26) == [1, 0, 0, 1]


def test_should_return_different_lastone() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]

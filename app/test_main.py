from app import main


def test_zero() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_one() -> None:
    assert main.get_coin_combination(1) == [1, 0, 0, 0]


def test_four() -> None:
    assert main.get_coin_combination(4) == [4, 0, 0, 0]


def test_five() -> None:
    assert main.get_coin_combination(5) == [0, 1, 0, 0]


def test_six() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]


def test_nine() -> None:
    assert main.get_coin_combination(9) == [4, 1, 0, 0]


def test_ten() -> None:
    assert main.get_coin_combination(10) == [0, 0, 1, 0]


def test_eleven() -> None:
    assert main.get_coin_combination(11) == [1, 0, 1, 0]


def test_seventeen() -> None:
    assert main.get_coin_combination(17) == [2, 1, 1, 0]


def test_twenty_four() -> None:
    assert main.get_coin_combination(24) == [4, 0, 2, 0]


def test_twenty_five() -> None:
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_twenty_six() -> None:
    assert main.get_coin_combination(26) == [1, 0, 0, 1]


def test_forty_one() -> None:
    assert main.get_coin_combination(41) == [1, 1, 1, 1]


def test_fifty() -> None:
    assert main.get_coin_combination(50) == [0, 0, 0, 2]

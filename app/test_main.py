from app.main import get_coin_combination


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_six_cents() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_seventeen_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_fifty_cents() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_two_pennies() -> None:
    assert get_coin_combination(2) == [2, 0, 0, 0]


def test_three_pennies() -> None:
    assert get_coin_combination(3) == [3, 0, 0, 0]


def test_four_pennies() -> None:
    assert get_coin_combination(4) == [4, 0, 0, 0]


def test_eleven_cents() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_nine_cents() -> None:
    assert get_coin_combination(9) == [4, 1, 0, 0]


def test_fifteen_cents() -> None:
    assert get_coin_combination(15) == [0, 1, 1, 0]


def test_twenty_cents() -> None:
    assert get_coin_combination(20) == [0, 0, 2, 0]


def test_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_fifty_one_cents() -> None:
    assert get_coin_combination(51) == [1, 0, 0, 2]


def test_seventy_five_cents() -> None:
    assert get_coin_combination(75) == [0, 0, 0, 3]


def test_ninety_nine_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_one_dollar() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_two_dollars() -> None:
    assert get_coin_combination(200) == [0, 0, 0, 8]


def test_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_thirteen_cents() -> None:
    assert get_coin_combination(13) == [3, 0, 1, 0]


def test_forty_one_cents() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]

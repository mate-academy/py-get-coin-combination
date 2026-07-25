from app.main import get_coin_combination


# write your tests here
def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_five_cents() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_ten_cents() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_twenty_five_cents() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_thirty_cents() -> None:
    assert get_coin_combination(30) == [0, 1, 0, 1]


def test_sixty_cents() -> None:
    assert get_coin_combination(60) == [0, 0, 1, 2]


def test_one_hundred_cents() -> None:
    assert get_coin_combination(100) == [0, 0, 0, 4]


def test_large_number() -> None:
    assert get_coin_combination(123) == [3, 0, 2, 4]


def test_with_extra_penny() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


def test_combination_one() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]


def test_combination_two() -> None:
    assert get_coin_combination(58) == [3, 1, 0, 2]


def test_combination_three() -> None:
    assert get_coin_combination(73) == [3, 0, 2, 2]


def test_combination_four() -> None:
    assert get_coin_combination(11) == [1, 0, 1, 0]


def test_combination_five() -> None:
    assert get_coin_combination(37) == [2, 0, 1, 1]

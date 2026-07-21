from app.main import get_coin_combination


def test_result_equals_zero_when_cents_equal_zero() -> None:
    assert (get_coin_combination(0) == [0, 0, 0, 0])


def test_result_when_cents_equal_one() -> None:
    assert (get_coin_combination(1) == [1, 0, 0, 0])


def test_result_when_cents_equal_six() -> None:
    assert (get_coin_combination(6) == [1, 1, 0, 0])


def test_result_when_cents_equal_sixteen() -> None:
    assert (get_coin_combination(16) == [1, 1, 1, 0])


def test_result_when_cents_equal_twenty_six() -> None:
    assert (get_coin_combination(26) == [1, 0, 0, 1])


def test_result_when_cents_equal_forty_one() -> None:
    assert (get_coin_combination(41) == [1, 1, 1, 1])


def test_result_when_cents_is_a_big_number() -> None:
    assert (get_coin_combination(148) == [3, 0, 2, 5])

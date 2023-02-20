from app.main import get_coin_combination


def test_when_only_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_get_coin_combination() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]

from app.main import get_coin_combination


def test_should_return_list() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_different_cents() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]

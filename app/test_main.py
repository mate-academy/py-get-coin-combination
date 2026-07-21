from app.main import get_coin_combination


def test_random_integers() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]

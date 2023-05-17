from app.main import get_coin_combination


def test_get_coin_combination_results() -> None:
    assert get_coin_combination(72) == [2, 0, 2, 2]

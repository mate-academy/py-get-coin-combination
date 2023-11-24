from app.main import get_coin_combination


def test_should_return_correct_sum() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]

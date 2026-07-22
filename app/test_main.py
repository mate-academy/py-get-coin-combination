from app.main import get_coin_combination


def test_func_should_return_the_right_result() -> None:
    assert get_coin_combination(41) == [1, 1, 1, 1]

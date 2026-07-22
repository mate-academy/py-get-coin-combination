from app.main import get_coin_combination


def test_should_return_different_coins() -> None:
    assert (
        get_coin_combination(41) == [1, 1, 1, 1]
    )

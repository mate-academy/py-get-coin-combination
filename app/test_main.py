from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]

    assert get_coin_combination(15) == [0, 1, 1, 0]

    assert get_coin_combination(1) == [1, 0, 0, 0]

    assert get_coin_combination(64) == [4, 0, 1, 2]

from app.main import get_coin_combination


def test_get_coin_combination() -> None:
    coins = get_coin_combination(1)

    assert coins == [0, 0, 0, 1]

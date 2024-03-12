from app.main import get_coin_combination


def test_different_types() -> None:
    assert get_coin_combination(44) == [4, 1, 1, 1]

from app.main import get_coin_combination


def test_1_cent() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0], \
        "Should return [1, 0, 0, 0]"


def test_7_cent() -> None:
    assert get_coin_combination(7) == [2, 1, 0, 0], \
        "Should return [2, 1, 0, 0]"


def test_19_cent() -> None:
    assert get_coin_combination(19) == [4, 1, 1, 0], \
        "Should return [4, 1, 1, 0]"


def test_67_cent() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2], \
        "Should return [2, 1, 1, 2]"

from app import main


def test_get_coin_combination() -> None:
    assert main.get_coin_combination(1) == [1, 0, 0, 0]
    assert main.get_coin_combination(5) == [0, 1, 0, 0]
    assert main.get_coin_combination(6) == [1, 1, 0, 0]
    assert main.get_coin_combination(10) == [0, 0, 1, 0]
    assert main.get_coin_combination(17) == [2, 1, 1, 0]
    assert main.get_coin_combination(25) == [0, 0, 0, 1]
    assert main.get_coin_combination(50) == [0, 0, 0, 2]
    assert main.get_coin_combination(0) == [0, 0, 0, 0]

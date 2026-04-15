from app import main


def test_examples_mix_types() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]
    assert main.get_coin_combination(17) == [2, 1, 1, 0]
    assert main.get_coin_combination(99) == [4, 0, 2, 3]

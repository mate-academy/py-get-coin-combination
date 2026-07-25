import app.main as main


def test_zero() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]


def test_small_values() -> None:
    assert main.get_coin_combination(1) == [1, 0, 0, 0]
    assert main.get_coin_combination(2) == [2, 0, 0, 0]
    assert main.get_coin_combination(4) == [4, 0, 0, 0]


def test_exact_coin_values() -> None:
    assert main.get_coin_combination(5) == [0, 1, 0, 0]
    assert main.get_coin_combination(10) == [0, 0, 1, 0]
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_mixed_values() -> None:
    assert main.get_coin_combination(6) == [1, 1, 0, 0]
    assert main.get_coin_combination(17) == [2, 1, 1, 0]
    assert main.get_coin_combination(41) == [1, 1, 1, 1]
    assert main.get_coin_combination(99) == [4, 0, 2, 3]


def test_sum_matches_amount() -> None:
    for cents in [0, 7, 13, 28, 41, 63, 87, 100]:
        result: list[int] = main.get_coin_combination(cents)
        values: list[int] = [1, 5, 10, 25]
        total: int = sum(result[i] * values[i] for i in range(4))
        assert total == cents


def test_length_is_four() -> None:
    assert len(main.get_coin_combination(50)) == 4

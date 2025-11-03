import importlib


main = importlib.import_module("app.main")


def test_returns_list_of_four_nonnegative_ints() -> None:
    res = main.get_coin_combination(0)
    assert isinstance(res, list), "result must be a list"
    assert len(res) == 4, "list must contain exactly four elements"
    assert all(isinstance(x, int) for x in res), \
        "all elements must be integers"
    assert all(x >= 0 for x in res), "all elements must be non-negative"


def test_examples_from_readme() -> None:
    # coins = [pennies, nickels, dimes, quarters]
    assert main.get_coin_combination(1) == [1, 0, 0, 0]
    assert main.get_coin_combination(6) == [1, 1, 0, 0]
    assert main.get_coin_combination(17) == [2, 1, 1, 0]
    assert main.get_coin_combination(50) == [0, 0, 0, 2]


def test_zero_and_single_quarter_cases() -> None:
    assert main.get_coin_combination(0) == [0, 0, 0, 0]
    assert main.get_coin_combination(25) == [0, 0, 0, 1]


def test_various_amounts_minimal_greedy_result() -> None:
    # 99 = 3*25 + 2*10 + 4*1  -> [4, 0, 2, 3]
    assert main.get_coin_combination(99) == [4, 0, 2, 3]
    # 41 = 1*25 + 1*10 + 1*5 + 1*1 -> [1, 1, 1, 1]
    assert main.get_coin_combination(41) == [1, 1, 1, 1]
    # 74 = 2*25 + 2*10 + 4*1 -> [4, 0, 2, 2]
    assert main.get_coin_combination(74) == [4, 0, 2, 2]

from app.main import get_coin_combination


# def test_get_coin_combination_one_cent() -> None:
#     assert get_coin_combination(1) == [1, 0, 0, 0]
#
#
# def test_get_coin_combination_five_cent() -> None:
#     assert get_coin_combination(6) == [1, 1, 0, 0]
#
#
# def test_get_coin_combination_ten_cent() -> None:
#     assert get_coin_combination(17) == [2, 1, 1, 0]
#
#
def test_get_coin_combination_all_cent() -> None:
    assert get_coin_combination(67) == [2, 1, 1, 2]

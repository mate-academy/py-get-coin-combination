from app.main import get_coin_combination


# write your tests here
def test_can_output_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_can_output_nickel() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_can_output_dime() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_can_output_quarter() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]

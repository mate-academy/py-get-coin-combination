from app.main import get_coin_combination


def test_returns_list_zeros_and_one_when_we_use_one_denomination() -> None:
    result = get_coin_combination(50)

    assert result == [0, 0, 0, 2]


def test_returns_list_num_when_we_use_not_one_denomination() -> None:
    result = get_coin_combination(17)

    assert result == [2, 1, 1, 0]

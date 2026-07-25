from app.main import get_coin_combination


def test_get_coin_combination_single_penny() -> None:
    result = get_coin_combination(1)
    assert result[0] == 1


def test_get_coin_combination_penny_and_nickel() -> None:
    result = get_coin_combination(6)
    assert result[0] == 1 and result[1] == 1


def test_get_coin_combination_multiple_coins() -> None:
    result = get_coin_combination(17)
    assert result[0] == 2 and result[1] == 1 and result[2] == 1


def test_get_coin_combination_quarters_only() -> None:
    result = get_coin_combination(50)
    assert result[3] == 2

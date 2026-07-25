from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "coin, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),


    ]
)
def test_get_coin_combination_various_thresholds(
        coin: int,
        expected_result: list) -> None:
    assert (
           get_coin_combination(coin) == expected_result)\
        , f"Should return {expected_result} for coins {coin})"


def test_get_coin_combination_error_on_invalid_types() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15")

    with pytest.raises(TypeError):
        get_coin_combination(2.5)


def test_get_coin_combination_raises_error_on_negative_numbers() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(0)
    with pytest.raises(ValueError):
        get_coin_combination(-1)

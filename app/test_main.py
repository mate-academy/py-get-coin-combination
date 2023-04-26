import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coin_value, excepted_value",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="Function should work correct with 0 value"
        ),

        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Function should work correct with normal value"
        ),

        pytest.param(
            17,
            [2, 1, 1, 0],
            id="Function should work correct with normal value"
        ),

        pytest.param(
            50,
            [0, 0, 0, 2],
            id="Function should work correct with normal value"
        )
    ])
def test_get_coin_combination(
        coin_value: int,
        excepted_value: list[int]
) -> None:
    assert get_coin_combination(coin_value) == excepted_value


@pytest.mark.parametrize(
    "coin_value, error",
    [
        pytest.param(
            "1",
            TypeError,
            id="Function should takes int. Not string!"
        ),

        pytest.param(
            [1],
            TypeError,
            id="Function should takes int. Not list!"
        )
    ])
def test_get_coin_combination_error(coin_value: int, error: TypeError) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(coin_value)

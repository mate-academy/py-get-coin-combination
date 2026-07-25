import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_coins,expected_result",
    [
        (
            1, [1, 0, 0, 0]
        ),
        (
            6, [1, 1, 0, 0]
        ),
        (
            17, [2, 1, 1, 0]
        ),
        (
            50, [0, 0, 0, 2]
        ),
        (
            117, [2, 1, 1, 4]
        )
    ]
)
def test_with_different_input(input_coins: int, expected_result: list) -> None:
    assert get_coin_combination(input_coins) == expected_result


@pytest.mark.parametrize(
    "input_coins,expected_error",
    [
        pytest.param(
            [1], TypeError,
            id="Should raise TypeError if value is invalid"
        ),
        pytest.param(
            "123", TypeError,
            id="Should raise TypeError if value is invalid"
        )
    ]
)
def test_should_return_correct_exception(
        input_coins: int, expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(input_coins)

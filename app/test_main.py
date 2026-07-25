import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(1, [1, 0, 0, 0], id="when amount is 1"),
        pytest.param(6, [1, 1, 0, 0], id="when amount is 6"),
        pytest.param(17, [2, 1, 1, 0], id="when amount is 6"),
        pytest.param(50, [0, 0, 0, 2], id="when amount is 50")

    ]
)
def test_should_return_expected_list_of_coins(
        cents: int,
        coins: list[int]) -> None:
    assert get_coin_combination(cents) == coins


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        pytest.param("12", TypeError, id="when input is string")

    ]
)
def test_should_raise_expected_error(cents: int | float | str | None,
                                     expected_error: Exception) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

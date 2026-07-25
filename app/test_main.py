from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert (get_coin_combination(cents) == result), (
        f"'get_coin_combination' must calculate "
        f"number coins in cents: {cents}")


def test_zero_argument() -> None:
    assert (get_coin_combination(0) == [0, 0, 0, 0]), (
        "'get_coin_combination' should return zero list"
    )


@pytest.mark.parametrize(
    "cents",
    [
        ("23"),
        ([17]),
        ({50}),
    ]
)
def test_rise_error_while_incorrect_arguments(cents: callable) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

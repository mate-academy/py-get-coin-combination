import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "number, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_coin_combination(number: int, result: list) -> None:
    assert (
        get_coin_combination(number) == result
    ), f"Coins should be {result}"


def test_raise_error_if_number_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("24")

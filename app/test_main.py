import pytest

from app.main import get_coin_combination


def test_input_value_typy() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("6")


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination_results(value: int, expected: list) -> None:
    assert (
        get_coin_combination(value) == expected
    ), f"With {value} expected {expected} but got {get_coin_combination(value)}"

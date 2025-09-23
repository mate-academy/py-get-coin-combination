import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
    ]
)
def test_function_should_be_correct_with_non_negative_values(
        cents: int,
        coins: list
) -> None:
    assert get_coin_combination(cents) == coins


def test_function_not_raise_exception_with_negative_input_data() -> None:
    assert get_coin_combination(-17) == [3, 1, 0, -1]


@pytest.mark.parametrize(
    "cents",
    [
        ("17"),
        ([17]),
    ]
)
def test_function_raise_error_if_input_datetype_not_integer(
        cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

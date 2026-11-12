from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "input_val, output",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        # (-1, [0, 0, 0, 0])
    ],
    ids=[
        "1 penny",
        "1 penny + 1 nickel",
        "2 pennies + 1 nickel + 1 dime",
        "2 quarters",
        "check zero",
        # "check negative input"
    ]
)
def test_get_coin_combination(input_val: int, output: list[int]) -> None:
    assert get_coin_combination(input_val) == output


@pytest.mark.parametrize(
    "call",
    [
        ("1"),
        ([1]),
        None
    ],
    ids=[
        "string",
        "list",
        "None"
    ]
)
def test_incorrect_type_of_input(call: None) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(call)

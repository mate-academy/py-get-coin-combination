import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (92809380983427293847928344, [4, 1, 1, 3712375239337091753917133]),
        (75, [0, 0, 0, 3]),
        (20, [0, 0, 2, 0]),
        (5, [0, 1, 0, 0]),
        (4, [4, 0, 0, 0])
    ],
    ids=[
        "if 0 cents is given",
        "if A LOT OF MONEY is provided",
        "when only quarter can be used",
        "when only dimes can be used",
        "when only nickels can be used",
        "when only pennies can be used"
    ]
)
def test_should_return_correct_combination(
    cents: int,
    expected: list
) -> None:
    assert get_coin_combination(cents) == expected


def test_should_raise_type_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("123")


def test_result_should_not_be_changed_by_previous_value() -> None:
    assert (
        get_coin_combination(66)
        is not get_coin_combination(91)
    )

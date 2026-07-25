import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="test should return zeros when cents is zero"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="test pennies number"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="test pennies and nickel numbers"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="test pennies, nickel and dimes numbers"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="test quarters number"
        )
    ]
)
def test_should_return_smallest_amount_of_coins(
    cents: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


def tesh_should_return_list_of_integers() -> None:
    for num in get_coin_combination(1):
        assert isinstance(num, int)


def test_should_raise_exception_if_cents_is_negative() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-5)

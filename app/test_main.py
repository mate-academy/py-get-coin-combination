import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_combination_possible_number(amount: int,
                                            expected: list) -> None:
    assert get_coin_combination(amount) == expected


@pytest.mark.parametrize(
    "amount",
    [
        ("6", ),
        (None, ),
        (4.5, ),
        (-3, )
    ]
)
def test_should_input_be_integer(amount: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(amount)

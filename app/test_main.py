from app.main import get_coin_combination
import pytest
from typing import Any


@pytest.mark.parametrize(
    "cents,list_of_quantity",
    [
        pytest.param(
            -1,
            [4, 0, 2, -1],
            id="cents should be greater -1"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny when cents equal 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1 penny and 1 nickel when cents equal 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 2 penny, 1 nickel and 1 dime when cents equal 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 2 quarter when cents equal 50"
        )
    ]
)
def test_return_correctly_list_money(
        cents: int,
        list_of_quantity: list
) -> None:
    assert get_coin_combination(cents) == list_of_quantity


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(
            "1",
            TypeError,
            id="should accept int type data"
        )
    ]
)
def test_raising_errors_correctly(
        cents: int,
        expected_error: Any
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

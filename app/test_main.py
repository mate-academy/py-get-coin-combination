import pytest

from typing import Any
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_right_value_output(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents,result,exception",
    [
        ("1", [1, 0, 0, 0], TypeError),
        ([5], [1, 1, 0, 0], TypeError),
        (17, 8, TypeError)
    ]
)
def test_input_incorrect_type(cents: Any,
                              result: Any,
                              exception: type[Exception]) -> None:
    with pytest.raises(exception):
        get_coin_combination(cents, result)

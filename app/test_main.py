from typing import Any

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3])
    ]
)
def test_should_work_with_normal_numbers(
        cents: int,
        result: list
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), "Incorrect combination of smallest possible number of coins"


@pytest.mark.parametrize(
    "cents, result",
    [
        (1999, [4, 0, 2, 79]),
        (1234567, [2, 1, 1, 49382]),
        (199999999999, [4, 0, 2, 7999999999]),
    ]
)
def test_should_work_with_large_numbers(
        cents: int,
        result: list
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), "Incorrect combination of smallest possible number of coins"


def test_should_return_list_of_zero_with_lack_of_coins() -> None:
    assert (
        get_coin_combination(0) == [0, 0, 0, 0]
    ), "Method should return [0, 0, 0, 0] with lack of coins"


@pytest.mark.parametrize(
    "cents",
    [
        "a",
        [1, 2],
        {"a": 1}
    ],
    ids=[
        "string types",
        "list type",
        "dict type"
    ]
)
def test_should_raise_error_with_incorrect_types(cents: Any) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_equal_expected_result(
    cents: int,
    expected_result: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents",
    [
        ("23",),
        (59.2,),
        ((2 + 5j),),
        (None,),
        ([],)
    ],
    ids=[
        "string",
        "float",
        "complex",
        "none-type",
        "list"
    ]
)
def test_should_raise_error_if_passed_incorrect_data_type(
    cents: Any
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents",
    [18, 24, 19, 34, 100]
)
def test_should_not_exceed_limits(cents: int) -> None:
    for money in get_coin_combination(cents):
        assert 0 <= money

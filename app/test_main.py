from app.main import get_coin_combination
import pytest


def test_an_array() -> bool:
    assert type(get_coin_combination(56)) == list


@pytest.mark.parametrize(
    "cents, expected",
    [
        (45, [0, 0, 2, 1]),
        (67, [2, 1, 1, 2]),
        (89, [4, 0, 1, 3]),
        (340, [0, 1, 1, 13]),
        (789, [4, 0, 1, 31]),
        (900, [0, 0, 0, 36]),

    ],
    ids=[
        "test_coin_45",
        "test_coin_67",
        "test_coin_89",
        "test_coin_340",
        "test_coin_789",
        "test_coin_900",
    ]
)
def test_main_get(cents: int, expected: int) -> int:
    result = get_coin_combination(cents)
    assert result == expected


def function_type_error(cents: int) -> list:
    result = get_coin_combination(cents)
    return result


@pytest.mark.parametrize(
    "cents, expected_error",
    [pytest.param("11", TypeError, id="data type check")]
)
def test_data_type_check(
        cents: int, expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        function_type_error(cents)

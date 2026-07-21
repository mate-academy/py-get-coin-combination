import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (25, [0, 0, 0, 1])
    ]
)
def test_returned_data_type(input_data: int, expected: list) -> None:
    result = get_coin_combination(input_data)
    assert isinstance(result, list), \
        f"Function must return list type, not {type(result)}"


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (101, [1, 0, 0, 1])
    ]
)
def test_returned_list_length(input_data: int, expected: list) -> None:
    assert len(get_coin_combination(input_data)) == 4, \
        "Length of list must be equal 4"


@pytest.mark.parametrize(
    "input_data,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (144, [4, 1, 1, 5])
    ]
)
def test_output_data(input_data: int, expected: list) -> None:
    assert get_coin_combination(input_data) == expected


@pytest.mark.parametrize(
    "input_data,expected",
    [
        ("123", TypeError),
        ([45], TypeError)
    ]
)
def test_exception_rising(input_data: int, expected: type(Exception)) -> None:
    with pytest.raises(expected):
        get_coin_combination(input_data)

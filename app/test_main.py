import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_value,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (769, [4, 1, 1, 30])
    ]
)
def test_function_must_return_correct_value(
        input_value: int,
        expected: int
) -> None:
    assert get_coin_combination(input_value) == expected


@pytest.mark.parametrize(
    "input_value,expected_error",
    [
        ({0}, TypeError),
        ([5], TypeError),
        ({4: 0}, TypeError),
        ((5,), TypeError),
        ("6", TypeError)
    ]
)
def test_function_must_raise_exception_if_input_type_is_incorrect(
        input_value: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(input_value)

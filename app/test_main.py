import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "given_coins,expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test should return list with four zeros"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test should return list: [1, 0, 0, 0]"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test should return list: [1, 1, 0, 0]"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test should return list: [2, 1, 1, 0]"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="test should return list: [1, 1, 1, 1]"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test should return list: [0, 0, 0, 2]"
        ),
        pytest.param(
            141,
            [1, 1, 1, 5],
            id="test should return list: [1, 1, 1, 5]"
        ),
    ]
)
def test_should_return_correct_lists_if_input_data_is_correct(
        given_coins: int,
        expected_result: list
) -> None:
    assert get_coin_combination(
        given_coins
    ) == expected_result, \
        f"if coins={given_coins} result should be {expected_result}"


@pytest.mark.parametrize(
    "incorrect_data,expected_error",
    [
        ({}, TypeError),
        ([], TypeError),
        ((), TypeError),
        (set, TypeError),
        ("some_text", TypeError)
    ]
)
def test_should_return_type_error_if_takes_incorrect_data_type(
        incorrect_data: set | tuple | dict | list | str,
        expected_error: TypeError
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(incorrect_data), \
            (f"test should return {expected_error} "
             f"if given data is {incorrect_data}")


def test_if_func_return_list_if_given_data_is_correct(
) -> None:
    assert type(get_coin_combination(1)) == list, \
        "func must return list"

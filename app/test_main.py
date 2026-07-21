import pytest


from app.main import get_coin_combination


def test_check_if_result_list_has_four_integers() -> None:
    assert (
        [type(element) == int for element in get_coin_combination(0)]
        == [True, True, True, True]
    ), "Results should have four integers"


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="Should return list of zeros, on zero coins"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="Should display pennies"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="Special case, one before nickle"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="Should display nickels"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="Special case, one before dime"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="Should display dimes"
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id="Special case, one before quarter"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="Should display quarters"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="One of each case"
        ),
        pytest.param(
            10**6 + 893,
            [3, 1, 1, 40035],
            id="Should work fine with big numbers"
        ),
    ]
)
def test_coin_combinations_input_result(
    cents: int,
    result: list
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"{cents} must result in {result}"

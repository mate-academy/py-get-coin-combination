import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            0, [0, 0, 0, 0], id="Nothing in input"
        ),
        pytest.param(
            1, [1, 0, 0, 0], id="1 penny to 1 cent"
        ),
        pytest.param(
            5, [0, 1, 0, 0], id="1 nickel to 5 cents"
        ),
        pytest.param(
            10, [0, 0, 1, 0], id="1 dime to 10 cents"
        ),
        pytest.param(
            25, [0, 0, 0, 1], id="1 quarter = 25 cents"
        ),
    ]
)
def test_check_one_coin_input(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            6, [1, 1, 0, 0], id="1penny_1nickel"
        ),
        pytest.param(
            17, [2, 1, 1, 0], id="2pennies_1nickel_1dime"
        ),
        pytest.param(
            41, [1, 1, 1, 1], id="1penny_1nickel_1dime_1quarter"
        ),
        pytest.param(
            99, [4, 0, 2, 3], id="4pennies_2dimes_3quarters"
        )
    ]
)
def test_different_coins_combinations(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            10, [0, 2, 0, 0], id="2 nickel to 10 cents"
        ),
    ]
)
def test_valid_of_output_result(
        cents: int,
        expected_result: list
) -> None:
    result = get_coin_combination(cents)
    assert isinstance(result, list) and len(result) == 4
    assert all(isinstance(x, int) and x >= 0 for x in result)


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            "one", ["one", "zero", 0, 0], id="not valid input"
        )
    ]
)
def test_check_valid_of_input(
        cents: int,
        expected_result: list
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

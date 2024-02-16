import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="should return array of zeros if cents equal to 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return 1 penny if cents equal to 1"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="should return 1 nickel if cents equal to 5"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should return 1 dime if cents equal to 10"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="should return 1 quarter if cents equal to 25"
        ),
    ]
)
def test_return_one_coin_if_cents_divided_by_one_of_coins(
        cents: int,
        expected_result: list[int]
) -> None:
    result = get_coin_combination(cents)

    assert result == expected_result


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            4, [4, 0, 0, 0],
            id="should return 4 pennies"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return 1 penny and 1 nickel"
        ),
        pytest.param(
            11, [1, 0, 1, 0],
            id="should return 1 penny and 1 dime"
        ),
        pytest.param(
            15, [0, 1, 1, 0],
            id="should return 1 nickel and 1 dime"
        ),
        pytest.param(
            16, [1, 1, 1, 0],
            id="should return 1 penny, 1 nickel and 1 dime"
        ),
        pytest.param(
            20, [0, 0, 2, 0],
            id="should return 2 dimes"
        ),
        pytest.param(
            21, [1, 0, 2, 0],
            id="should return 2 dimes and 1 penny"
        ),
        pytest.param(
            26, [1, 0, 0, 1],
            id="should return 1 quarter and 1 penny"
        ),
        pytest.param(
            30, [0, 1, 0, 1],
            id="should return 1 quarter and 1 nickel"
        ),
    ]
)
def test_return_minimal_combination_of_coins(
        cents: int,
        expected_result: list[int]
) -> None:
    result = get_coin_combination(cents)

    assert result == expected_result

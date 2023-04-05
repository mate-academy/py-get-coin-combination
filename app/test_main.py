import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_if_result_has_right_format(cents: int, expected_result: list) -> None:
    result = get_coin_combination(cents)
    assert (
        isinstance(result, list)
    ), "result should be list"
    assert (
        len(result) == 4
    ), "result list should have 4 items"
    assert (
        isinstance(result[0], int) and isinstance(result[1], int)
        and isinstance(result[2], int) and isinstance(result[3], int)
    ), "items of result should be int"


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_on_the_correct_distribution_of_coins(
        cents: int,
        expected_result: list
) -> None:
    assert (
        get_coin_combination(cents) == expected_result
    ), f"get_coin_combination for {cents} should be " \
       f"{expected_result[0]}, {expected_result[1]}, " \
       f" {expected_result[2]}, {expected_result[3]}"

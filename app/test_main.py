import pytest
from app import main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (2, [2, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (11, [1, 0, 1, 0]),
        (29, [4, 0, 0, 1]),
        (47, [2, 0, 2, 1]),
        (63, [3, 0, 1, 2]),
    ],
)
def test_get_coin_combination_parametrized(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [0, 1, 17, 42, 99, 250])
def test_result_is_list_of_four_elements(cents: int) -> None:
    result = main.get_coin_combination(cents)
    assert isinstance(result, list)
    assert len(result) == 4


@pytest.mark.parametrize("cents", [0, 1, 17, 42, 99, 250])
def test_total_value_matches_input(cents: int) -> None:
    result = main.get_coin_combination(cents)
    total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total == cents


@pytest.mark.parametrize("cents", [0, 1, 17, 42, 99, 250])
def test_all_coin_counts_are_non_negative(cents: int) -> None:
    result = main.get_coin_combination(cents)
    assert all(count >= 0 for count in result)

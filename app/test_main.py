import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (78, [3, 0, 0, 3]),
        (47, [2, 0, 2, 1]),
    ]
)
def test_check_test_coin_combinations(cents: int, coins_list: list) -> None:
    assert get_coin_combination(cents) == coins_list


@pytest.mark.parametrize(
    "type_error_cases",
    [
        [1],
        "10",
        {14},
        {0: 15}
    ]
)
def test_should_raises_type_error_exception(type_error_cases: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(type_error_cases)

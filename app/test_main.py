from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "count_cent, list_coins_res",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
)
def test_correct_result(count_cent: int, list_coins_res: list) -> None:
    goals = get_coin_combination(count_cent)
    assert goals == list_coins_res


@pytest.mark.parametrize(
    "count_cent, len_list_coins_res",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (4, [4, 0, 0, 0])
    ],
)
def test_return_only_pennies(
        count_cent: int,
        len_list_coins_res: list
) -> None:
    goals = get_coin_combination(count_cent)
    assert goals == len_list_coins_res


@pytest.mark.parametrize(
    "count_cent, list_coins_res",
    [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (67, [2, 1, 1, 2])
    ],
)
def test_return_only_one_type(count_cent: int, list_coins_res: list) -> None:
    goals = get_coin_combination(count_cent)
    assert goals == list_coins_res


@pytest.mark.parametrize(
    "count_cent, list_coins_res",
    [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
)
def test_should_return_list(count_cent: int, list_coins_res: list) -> None:
    goals = get_coin_combination(count_cent)
    assert isinstance(goals, list)

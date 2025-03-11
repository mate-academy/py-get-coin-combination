import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result, id",
    [
        (1, [1, 0, 0, 0], "get_coin_combination_one_cent"),
        (6, [1, 1, 0, 0], "get_coin_combination_six_cents"),
        (17, [2, 1, 1, 0], "get_coin_combination_seventeen_cents"),
        (50, [0, 0, 0, 2], "get_coin_combination_fifty_cents"),
    ]
)
def test_get_coin_combination(cents: int, expected_result: list, id) -> None:
    result = get_coin_combination(cents)
    assert result == expected_result, (
        f"Result should be {expected_result}"
    )


@pytest.mark.parametrize(
    "cents, id",
    [
        (1, "data_type_check_for_1_cent"),
        (6, "data_type_check_for_6_cent"),
        (17, "data_type_check_for_17_cent"),
        (50, "data_type_check_for_50_cent"),
    ]
)
def test_data_type_of_cents(cents: int, id) -> None:
    assert isinstance(cents, int), (
        f"Cents should be int"
    )

@pytest.mark.parametrize(
    "cents, expected_result, id",
    [
        (1, [1, 0, 0, 0], "data_type_check_for_result_(cents=1)"),
        (6, [1, 1, 0, 0], "data_type_check_for_result_(cents=6)"),
        (17, [2, 1, 1, 0], "data_type_check_for_result_(cents=17)"),
        (50, [0, 0, 0, 2], "data_type_check_for_result_(cents=50)"),
    ]
)
def test_data_type_of_result(cents: int, expected_result: list, id) -> None:
    result = get_coin_combination(cents)
    assert isinstance(result, list), (
        "Result should be list"
    )

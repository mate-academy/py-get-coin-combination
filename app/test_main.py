import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0],),
        (6, [1, 1, 0, 0],),
        (17, [2, 1, 1, 0],),
        (50, [0, 0, 0, 2],),
    ],
    ids=[
        "Test for 1 cent",
        "Test for 6 cents",
        "Test for 17 cents",
        "Test for 50 cents"
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    result = get_coin_combination(cents)
    assert result == expected_result, (
        f"Result should be {expected_result}"
    )


@pytest.mark.parametrize(
    "cents",
    [
        1,
        6,
        17,
        50,
    ],
    ids=[
        "Test for data type of 1 cent",
        "Test for data type of 6 cents",
        "Test for data type of 17 cents",
        "Test for data type of 50 cents"
    ]
)
def test_data_type_of_cents(cents: int) -> None:
    assert isinstance(cents, int), (
        "Cents should be int"
    )


@pytest.mark.parametrize(
    "cents",
    [
        1,
        6,
        17,
        50,
    ],
    ids=[
        "Test for result type when cents = 1",
        "Test for result type when cents = 6",
        "Test for result type when cents = 17",
        "Test for result type when cents = 50"
    ]
)
def test_data_type_of_result(cents: int) -> None:
    result = get_coin_combination(cents)
    assert isinstance(result, list), (
        "Result should be list"
    )

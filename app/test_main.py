import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (1234567, [2, 1, 1, 49382]),
    ],
    ids=[
        "Testing for 1 cent",
        "Tesing for 6 cents",
        "Testing for 17 cents",
        "Testing for 50 cents",
        "Testing for huge amount of cents"
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents, error",
    [
        ("10", TypeError)
    ]
)
def test_get_coin_combination_for_errors(cents: int, error: Exception) -> None:
    with pytest.raises(error):
        get_coin_combination(cents)

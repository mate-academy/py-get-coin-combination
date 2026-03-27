import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_function_returns_expected_list(cents: int,
                                        coins: list) -> None:
    result = get_coin_combination(cents)

    assert result == coins

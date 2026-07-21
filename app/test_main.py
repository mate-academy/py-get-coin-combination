import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return [0, 0, 0, 0] if cents is zero "
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return [1, 1, 1, 1] if cents is 41 "
        )
    ]
)
def test_return_coins_correctly(
        cents: int,
        expected_coins: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_coins

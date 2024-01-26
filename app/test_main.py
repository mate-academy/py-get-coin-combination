import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_combination_cents",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (18, [3, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (68, [3, 1, 1, 2]),
    ],
    ids=[
        "0 coins should be convert to combination [0, 0, 0, 0]",
        "1 coins should be convert to combination [1, 0, 0, 0]",
        "6 coins should be convert to combination [1, 1, 0, 0]",
        "18 coins should be convert to combination [3, 1, 1, 0]",
        "50 coins should be convert to combination [0, 0, 0, 2]",
        "68 coins should be convert to combination [3, 1, 1, 2]",
    ]
)
def test_should_correctly_return_coordination(
        cents: int,
        expected_combination_cents: list
) -> None:
    assert get_coin_combination(cents) == expected_combination_cents

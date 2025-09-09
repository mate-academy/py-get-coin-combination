import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_get_coin_combination_examples(cents: int,
                                       expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [100, 250, 999])
def test_get_coin_combination_large_numbers(cents: int) -> None:
    result: list[int] = get_coin_combination(cents)
    total = result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    assert total == cents
    for i, coin_value in enumerate([1, 5, 10, 25]):
        if result[i] > 0:
            smaller = result.copy()
            smaller[i] -= 1
            new_total = (
                smaller[0] * 1 + smaller[1] * 5
                + smaller[2] * 10 + smaller[3] * 25
            )
            assert new_total != cents

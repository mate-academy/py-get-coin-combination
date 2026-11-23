import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_should_return_combination_as_in_examples(
        cents: int,
        expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


def test_should_return_zeros_when_cents_is_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (99, [4, 0, 2, 3]),
    ],
)
def test_should_use_biggest_coins_first_on_boundaries(
        cents: int,
        expected: list[int],
) -> None:
    assert get_coin_combination(cents) == expected


def test_should_return_list_of_four_elements() -> None:
    result = get_coin_combination(41)
    assert isinstance(result, list)
    assert len(result) == 4
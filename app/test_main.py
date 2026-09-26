import pytest
from app.main import get_coin_combination


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_penny() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_one_nickel() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


def test_one_dime() -> None:
    assert get_coin_combination(10) == [0, 0, 1, 0]


def test_one_quarter() -> None:
    assert get_coin_combination(25) == [0, 0, 0, 1]


def test_examples_from_task() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]
    assert get_coin_combination(17) == [2, 1, 1, 0]
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_boundary_99_cents() -> None:
    assert get_coin_combination(99) == [4, 0, 2, 3]


@pytest.mark.parametrize(
    "cents, expected",
    [
        (4, [4, 0, 0, 0]),
        (11, [1, 0, 1, 0]),
        (15, [0, 1, 1, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_various_combinations(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected

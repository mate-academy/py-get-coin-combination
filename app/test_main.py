import pytest

from app.main import get_coin_combination


def test_zero() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


@pytest.mark.parametrize(
    "input_,output_",
    [
        (25, [0, 0, 0, 1]),
        (75, [0, 0, 0, 3]),
        (100, [0, 0, 0, 4]),
        (250, [0, 0, 0, 10])
    ]
)
def test_only_quarters(
        input_: int,
        output_: int
) -> None:
    assert get_coin_combination(input_) == output_


@pytest.mark.parametrize(
    "input_,output_",
    [
        (20, [0, 0, 2, 0]),
        (10, [0, 0, 1, 0]),
    ]
)
def test_only_dimes(
        input_: int,
        output_: int
) -> None:
    assert get_coin_combination(input_) == output_


def test_only_nickels() -> None:
    assert get_coin_combination(5) == [0, 1, 0, 0]


@pytest.mark.parametrize(
    "input_,output_",
    [
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (3, [3, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
    ]
)
def test_only_pennies(
        input_: int,
        output_: int
) -> None:
    assert get_coin_combination(input_) == output_


@pytest.mark.parametrize(
    "input_,output_",
    [
        (41, [1, 1, 1, 1]),
        (123, [3, 0, 2, 4]),
        (54, [4, 0, 0, 2]),
        (67, [2, 1, 1, 2]),
    ]
)
def test_combinations(
        input_: int,
        output_: int
) -> None:
    assert get_coin_combination(input_) == output_

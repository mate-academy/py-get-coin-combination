import pytest

from app.main import get_coin_combination


def test_len_must_be_4_and_type_must_be_list() -> None:
    result = get_coin_combination(4)
    assert isinstance(result, list)
    assert len(result) == 4


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ],
)
def test_key_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2])
    ]
)
def test_simple_combination_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected",
    [
        (254, [4, 0, 0, 10]),
        (320, [0, 0, 2, 12]),
        (521, [1, 0, 2, 20]),
        (999, [4, 0, 2, 39])
    ]
)
def test_large_cases(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

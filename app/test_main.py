import pytest
from app import main


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (41, [1, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected",
    [
        ("15", 15),
        (15, "15"),
        ("cat", "dog"),
        (1.5, 15),
        (15, 1.5),
        (None, 15),
        (15, None),
    ]
)
def test_get_coin_combination_invalid_types(cents: int, expected: int) -> None:
    with pytest.raises((TypeError, ValueError)):
        main.get_coin_combination(cents, expected)

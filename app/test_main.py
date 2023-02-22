import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (82, [2, 1, 0, 3]),
    ],
    ids=[
        "0, should return [0, 0, 0, 0]",
        "1, should return [1, 0, 0, 0]",
        "6, should return [1, 1, 0, 0]",
        "16, should return [1, 1, 1, 0]",
        "41, should return [1, 1, 1, 1]",
        "82 should return [2, 1, 0, 3]",
    ]
)
def test_get_coin_combination(cents: int, expected_list: list) -> None:
    assert get_coin_combination(cents) == expected_list


@pytest.mark.parametrize("cents, expected_list", [
    ("1", TypeError),
    ([2], TypeError),
    ({"4": 4}, TypeError),
])
def test_get_coin_combination_error(
        cents: int,
        expected_list: list,
) -> None:
    with pytest.raises(expected_list):
        get_coin_combination(cents)

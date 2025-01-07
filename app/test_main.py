import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "0 cent",
        "1 cent",
        "6 cent",
        "17 cent",
        "50 cent"
    ]
)
def test_get_coin_combination(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result

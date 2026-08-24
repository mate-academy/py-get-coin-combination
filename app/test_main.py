import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, expected",
    [
        (
            0,
            [0, 0, 0, 0],
        ),
        (
            1,
            [1, 0, 0, 0],
        ),
        (
            4,
            [4, 0, 0, 0],
        ),
        (
            5,
            [0, 1, 0, 0],
        ),
        (
            9,
            [4, 1, 0, 0],
        ),
        (
            10,
            [0, 0, 1, 0],
        ),
        (
            24,
            [4, 0, 2, 0],
        ),
        (
            25,
            [0, 0, 0, 1],
        ),
        (
            41,
            [1, 1, 1, 1],
        ),
    ]
)
def test_bound_values(cent: int, expected: list) -> None:
    assert get_coin_combination(cent) == expected

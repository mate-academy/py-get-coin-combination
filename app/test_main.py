import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_output",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),

        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (24, [4, 0, 2, 0]),

        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),

        (100, [0, 0, 0, 4]),
        (1000, [0, 0, 0, 40])
    ]
)
def test_get_coin_combination(
        cents: int,
        expected_output: list
) -> None:
    assert get_coin_combination(cents) == expected_output

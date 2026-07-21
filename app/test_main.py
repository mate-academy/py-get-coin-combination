import pytest

from app import main


@pytest.mark.parametrize(
    "cents,expected_combination",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination(
    cents: int, expected_combination: list
) -> None:
    actual_combination = main.get_coin_combination(cents)

    assert actual_combination == expected_combination, (
        f"For {cents} cents, expected combination {expected_combination}, "
        f"but got {actual_combination}"
    )

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected_combination", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])
])
def test_result_combination(
        cents: int, expected_combination: int
) -> None:
    assert get_coin_combination(cents) == expected_combination

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cent, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ])
def test_coin_combination(cent: int, expected_result: list) -> None:
    assert get_coin_combination(cent) == expected_result

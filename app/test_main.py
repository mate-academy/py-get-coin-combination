from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "initialize, expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (7, [2, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0]),
        (2000, [0, 0, 0, 80])

    ]
)
def test_for_correct_expected_result(
        initialize: int,
        expected_result: list
) -> None:
    assert get_coin_combination(initialize) == expected_result

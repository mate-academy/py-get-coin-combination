import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (-333, [0, 0, 0, 0]),
        (-7, [0, 0, 0, 0]),
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (53, [3, 0, 0, 2]),
        (10011, [1, 0, 1, 400])
    ]
)
def test_should_return_correct_coin_combination(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result

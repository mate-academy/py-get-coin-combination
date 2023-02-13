from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4]),
    ]
)
def test_should_return_expected_values(cents: int, result: int) -> None:
    assert (
        get_coin_combination(cents) == result
    ), (
        f"if cents == {cents}, result should be {result}"
    )

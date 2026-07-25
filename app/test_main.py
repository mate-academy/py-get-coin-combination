import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (100, [0, 0, 0, 4])
    ]
)
def test_check_input_value(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"{cents} cents is {result} coin."

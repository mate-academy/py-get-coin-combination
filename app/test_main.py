import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,correct_output",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test for single penny"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test for zero"
        ),
        pytest.param(
            -15,
            [0, 0, 0, 0],
            id="test for negative number"
        ),
        pytest.param(
            555,
            [0, 1, 0, 22],
            id="test for big number"
        ),
    ]
)
def test_func(cents: int, correct_output: list) -> None:
    assert get_coin_combination(cents) == correct_output

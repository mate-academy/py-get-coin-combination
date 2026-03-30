import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="check if function returns only quarters"
        ),
        pytest.param(
            20,
            [0, 0, 2, 0],
            id="check if function returns only dimes"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="check if function returns only nickels"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="check if function returns only pennies"
        ),
        pytest.param(
            93,
            [3, 1, 1, 3],
            id="check if function returns all coins"
        )
    ]
)
def test_get_correct_answers(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result

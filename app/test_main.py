import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins,result", [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1]),
        (43, [3, 1, 1, 1])
    ]
)
def test_if_get_coin_combination_works_correct(
    coins: int,
    result: list
) -> None:
    assert (get_coin_combination(coins) == result
            ), f"{get_coin_combination(coins)} should be equal to {result}."

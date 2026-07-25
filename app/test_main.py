from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_combination",
    [
        pytest.param(
            -10, [0, 1, 1, -1],
            id="check with negative cents"
        ),

        pytest.param(
            0, [0, 0, 0, 0],
            id="check with zero cents"
        ),

        pytest.param(
            1, [1, 0, 0, 0],
            id="only 1 cents"
        ),

        pytest.param(
            5, [0, 1, 0, 0],
            id="just 5 cents"
        ),

        pytest.param(
            10, [0, 0, 1, 0],
            id="just 10 cents"
        ),

        pytest.param(
            25, [0, 0, 0, 1],
            id="just 25 cents"
        ),

        pytest.param(
            19, [4, 1, 1, 0],
            id="with not double small number of cents"
        ),

        pytest.param(
            533, [3, 1, 0, 21],
            id="with not double big number of cents"
        ),

        pytest.param(
            345971, [1, 0, 2, 13838],
            id="with not double very big number of cents"
        ),
    ]
)
def test_different_ways(cents: int, expected_combination: list) -> None:
    assert get_coin_combination(cents) == expected_combination

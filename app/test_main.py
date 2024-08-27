import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="should return empty list when 0 cents"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return [1, 0, 0, 0] when 1 cent"
        ),
        pytest.param(
            4, [4, 0, 0, 0],
            id="should return [4, 0, 0, 0] when 4 cents"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="should return [0, 1, 0, 0] when 5 cents"
        ),
        pytest.param(
            9, [4, 1, 0, 0],
            id="should return [4, 0, 0, 0] when 4 cents"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="should return [0, 0, 1, 0] when 10 cents"
        ),
        pytest.param(
            24, [4, 0, 2, 0],
            id="should return [4, 0, 2, 0] when 24 cent"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="should return [0, 0, 0, 1] when 25 cents"
        ),
        pytest.param(
            117, [2, 1, 1, 4],
            id="should return [2, 1, 1, 4] when 117 cents"
        )

    ]

)
def test_get_coin_combination_calculate_correctly(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents, error",
    [
        pytest.param(
            "0", TypeError,
            id="should return error when cents str"
        ),
        pytest.param(
            [0], TypeError,
            id="should return error when cents list"
        ),

    ]

)
def test_get_coin_combination_raise_correct_errors(
        cents: Any,
        error: Exception
) -> None:
    with pytest.raises(error):
        get_coin_combination(cents)

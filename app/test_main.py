from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "amount_to_convert,extend_value",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="CHECKING NULL VALUE"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="limit value check"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="limit value check"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="limit value check"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="limit value check"
        ),
        pytest.param(
            24,
            [4, 0, 2, 0],
            id="limit value check"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="limit value check"
        ),
        pytest.param(
            500,
            [0, 0, 0, 20],
            id="limit value check"
        )
    ]
)
def test_coim(amount_to_convert: int, extend_value: list) -> None:
    assert get_coin_combination(amount_to_convert) == extend_value

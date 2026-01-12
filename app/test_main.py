import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zero if cents 0"
        ),
        pytest.param(
            7,
            [2, 1, 0, 0],
            id="should return nickel if cents > 5"
        ),
        pytest.param(
            18,
            [3, 1, 1, 0],
            id="should return dime if cents > 10"
        ),
        pytest.param(
            67,
            [2, 1, 1, 2],
            id="should return quarter if cents > 25"
        ),
        pytest.param(
            2193,
            [3, 1, 1, 87],
            id="result should be correct when cents is large"
        ),
    ]
)
def test_modify_get_coin_combination_correctly(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result

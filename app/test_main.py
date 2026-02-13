import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,values",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="when value is 1 cent should return 1"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="17 cents"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="50 cents"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="return empty list if cents is 0"
        ),
        pytest.param(
            127,
            [2, 0, 0, 5]
        ),
        pytest.param(
            99,
            [4, 0, 2, 3]
        ),
        pytest.param(
            24,
            [4, 0, 2, 0]
        ),
        pytest.param(
            1000,
            [0, 0, 0, 40]
        ),
        pytest.param(
            5,
            [0, 1, 0, 0]
        )
    ]
)
def test_get_coin_combination(cents, values):
    assert get_coin_combination(cents) == values
    assert len(get_coin_combination(cents)) == 4

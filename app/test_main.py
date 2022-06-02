import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test for one cent"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test for six cents"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test for 17 cents"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test for 50 cents"
        )
    ]
)
def test_get_coin_combination(cents, result):
    assert get_coin_combination(cents) == result

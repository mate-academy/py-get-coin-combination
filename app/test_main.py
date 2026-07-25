import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="1 cent is 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="6 cents is 1 penny and 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="17 cents is 2 pennies, 1 nickel and 1 dime"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="50 cents is 2 quarters"
        ),
        pytest.param(
            100,
            [0, 0, 0, 4],
            id="100 cents is 4 quarters"
        ),
        pytest.param(
            1000,
            [0, 0, 0, 40],
            id="1000 cents is 40 quarters"
        ),
        pytest.param(
            1111,
            [1, 0, 1, 44],
            id="1111 cents is 1 penny, 1 dime and 44 quarters"
        ),
    ]
)
def test_get_coin_combination(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

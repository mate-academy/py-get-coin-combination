from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="should return 0's when cents are 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return 1 penny when cents are 1"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return 1 penny, 1 nickel when cents are 6"
        ),
        pytest.param(
            16, [1, 1, 1, 0],
            id="should return 1 penny, 1 nickel, 1 dime when cents are 16"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id=("should return 1 penny, 1 nickel, "
                "1 dime, 1 quarter when cents are 41")
        ),
    ]
)
def test_get_coin_combination(cents: int, expected: list):
    assert get_coin_combination(cents) == expected

import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, combination",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return all zeros if cents is 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return 1 penny, if cents is 1"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return 1 penny and 1 nickel, if cents is 6"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should return 2 penny, 1 nickel and 1 dime ,if cents is 17"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should return 2 quarters, if cents is 50"
        )
    ]
)
def test_get_coin_combination(cents: int, combination: list) -> None:
    assert get_coin_combination(cents) == combination

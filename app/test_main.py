import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [pytest.param(
        1,
        [1, 0, 0, 0],
        id="test with 1 cent 1 penny"
    ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test with 1 penny + 1 nickel"
    ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test with 2 penny, 1 nickel and 1 dime"
    ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test with 2 quarters"
    )]
)
def test_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

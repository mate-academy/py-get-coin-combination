import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert (get_coin_combination(cents) == expected
            ), f"Result should be equal to {expected}"


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(
            -3,
            ValueError,
            id="should raise error when cents is negative"),
        pytest.param(
            "5",
            TypeError,
            id="should raise error when cents is not integer"),
    ]
)
def check_errors(cents: int) -> None:
    get_coin_combination(cents)

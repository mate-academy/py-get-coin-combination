from app.main import get_coin_combination
import pytest


def test_return_type() -> None:
    assert isinstance(get_coin_combination(1), list)


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zero"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should convert to nickel correctly"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should convert to dime correctly"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should convert to quarter correctly"
        ),
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result

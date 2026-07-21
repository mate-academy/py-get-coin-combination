import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_count, expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test when cents isn't defined"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test when penny is defined"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test when nickel is defined"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test when dime is defined"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test when quarters is defined"
        )
    ]
)
def test_get_coin_combination(input_count: int, expected: list) -> None:
    assert get_coin_combination(input_count) == expected

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
        ),
        pytest.param(
            6,
            [1, 1, 0, 0]
        ),
        pytest.param(
            17,
            [2, 1, 1, 0]
        ),
        pytest.param(
            50,
            [0, 0, 0, 2]
        )
    ]
)
def test_should_convert_correctly(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result

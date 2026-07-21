from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
        ),
        pytest.param(
            10,
            [0, 0, 1, 0]
        ),
        pytest.param(
            21,
            [1, 0, 2, 0]
        ),
        pytest.param(
            55,
            [0, 1, 0, 2]
        )
    ]
)
def test_should_convert_correctly(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result

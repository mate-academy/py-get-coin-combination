from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            -5,
            [0, 0, 0, 0],
            id="should treat negative numbers as zero"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return 4 zeros when 0 cents given"
        ),
        pytest.param(
            83,
            [3, 1, 0, 3],
            id="should place coins correctly"
        )
    ]
)
def test_should_convert_correctly(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result

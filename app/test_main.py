from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test should return empty list when 0 cents"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test should return 1 penny as result"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="test should return 1 nickel"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test should return 1 penny and 1 nickel"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="test should return 1 dime"
        ),
        pytest.param(
            16,
            [1, 1, 1, 0],
            id="test should return 1 penny, 1 nickel and 1 dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="test should return 1 quarter"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="test should return 1 penny, 1 nickel, 1 dime, 1 quarter"
        ),
        pytest.param(
            65754647474,
            [4, 0, 2, 2630185898],
            id="test should return correct result with large numbers"
        )
    ]
)
def test_should_return_correct_value(cents: int,
                                     expected_result: list[int]) -> None:
    assert (
        get_coin_combination(cents) == expected_result
    )

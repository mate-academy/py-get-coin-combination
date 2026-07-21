import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, expected_result",
    [
        pytest.param(1, [1, 0, 0, 0], id="test for 1 cent"),
        pytest.param(6, [1, 1, 0, 0], id="test for 6 cent"),
        pytest.param(17, [2, 1, 1, 0], id="test for 17 cent"),
        pytest.param(50, [0, 0, 0, 2], id="test for 50 cent"),
    ]
)
def test_function_get_coin_combination(
        cent: int,
        expected_result: list
) -> bool:
    assert get_coin_combination(cent) == expected_result

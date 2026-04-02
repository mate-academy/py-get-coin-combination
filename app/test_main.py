import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, result",
    [
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2]),
        pytest.param(0, [0, 0, 0, 0])
    ]
)
def test_modify_correctly(cent: int, result: list) -> None:
    assert get_coin_combination(cent) == result

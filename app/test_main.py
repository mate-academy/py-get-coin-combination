from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cent,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_should_return_correct_result(cent: int, result: list) -> None:
    assert get_coin_combination(cent) == result

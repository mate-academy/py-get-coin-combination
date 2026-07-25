import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount,result",
    [
        (1, [1, 0, 0, 0]),
        (43, [3, 1, 1, 1]),
        (532, [2, 1, 0, 21])
    ]
)
def test_correct_output(amount: int, result: list) -> None:
    assert get_coin_combination(amount) == result

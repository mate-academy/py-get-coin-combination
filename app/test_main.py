import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (100, [0, 0, 0, 4])
    ]
)
def test_get_coin_combination(value: int, result: list[int]) -> None:
    assert get_coin_combination(value) == result

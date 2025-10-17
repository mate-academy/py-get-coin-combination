import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,result",
    [
        (41, [1, 1, 1, 1]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (100, [0, 0, 0, 4]),
        (0, [0, 0, 0, 0])

    ]
)
def test_should_check_that_func_return_diff_coins(
        value,
        result
) -> None:
    assert get_coin_combination(value) == result

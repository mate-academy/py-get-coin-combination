import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "initial,expected",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="return zero if initial is zero"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="return 1 penny if initial is 1"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="return 1 nickel if initial is 5"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="return 1 dime if initial is 10"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="return 1 quarter if initial is 25"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="return 1 penny and 1 nickel if initial is 6"
        ),
        pytest.param(
            11, [1, 0, 1, 0],
            id="return 1 dime and 1 nickel if initial is 11"
        ),
        pytest.param(
            16, [1, 1, 1, 0],
            id="return 1 penny, 1 dime and 1 nickel if initial is 16"
        ),
        pytest.param(
            44, [4, 1, 1, 1],
            id="return 4 penny, 1 nickel, 1 dime and 1 quarter "
               "if initial is 44"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="return 2 quarters if initial is 50"
        )
    ]
)
def test_modify_coin_correctly(initial: int, expected: list) -> None:
    assert get_coin_combination(initial) == expected

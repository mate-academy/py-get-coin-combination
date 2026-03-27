import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "enter_value, expected_value",
    [
        pytest.param(
            1, [1, 0, 0, 0]
        ),
        pytest.param(
            6, [1, 1, 0, 0]
        ),
        pytest.param(
            17, [2, 1, 1, 0]
        ),
        pytest.param(
            50, [0, 0, 0, 2]
        )
    ]
)
def test_count_number_of_coins(
        enter_value: int,
        expected_value: list[int]
) -> None:
    assert get_coin_combination(enter_value) == expected_value

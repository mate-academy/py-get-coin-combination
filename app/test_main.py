import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_data,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="should return zeroes if input is 0"),
        pytest.param(24, [4, 0, 2, 0], id="should work with values below 25"),
        pytest.param(67, [2, 1, 1, 2], id="should return different coins"),
        pytest.param(98, [3, 0, 2, 3], id="should work with values baloe 100"),
        pytest.param(
            56.75,
            [1.0, 1.0, 0.0, 2.0],
            id="should word with float input"
        ),
        pytest.param(
            34567876543,
            [3, 1, 1, 1382715061],
            id="should work with large number"
        )
    ]
)
def test_get_coin_combination_with_different_inputs(
        input_data: int,
        result: list[int]
) -> None:
    assert get_coin_combination(input_data) == result


def test_error_rising_with_non_numeric_inputs() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("str")

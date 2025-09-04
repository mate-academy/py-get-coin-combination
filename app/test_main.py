from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "money_value,result_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        pytest.param(
            -1,
            [4, 0, 2, -1],
            id="negative number generation value errors"
        )
    ]
)
def test_logic_function_get_coin_combination(
    money_value: int,
    result_list: list
) -> None:

    assert get_coin_combination(money_value) == result_list


def test_type_error() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("10")

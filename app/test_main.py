from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "total_value, result",
    [
        pytest.param(
            16,
            [1, 1, 1, 0],
            id="low_value"
        ),
        pytest.param(
            86,
            [1, 0, 1, 3],
            id="medium_value"
        ),
        pytest.param(
            218,
            [3, 1, 1, 8],
            id="high_value"
        )
    ]
)
def test_get_coin_combination(total_value: int, result: list) -> None:
    assert get_coin_combination(total_value) == result


@pytest.mark.parametrize(
    "total_value",
    [
        pytest.param(
            "string",
            id="can't be string"
        ),
        pytest.param(
            [1, 2, 3],
            id="can't be list"
        ),
        pytest.param(
            None,
            id="can't be None"
        )
    ]
)
def test_get_coin_combination_invalid(total_value: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(total_value)

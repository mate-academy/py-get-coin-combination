import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_all_combinations(cent: int, result: list):
    assert get_coin_combination(cent) == result


def test_age_is_less_then_zero() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_age_is_not_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("10")
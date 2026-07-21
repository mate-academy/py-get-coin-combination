import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value, output",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_check_all_values(value: int, output: list[int]) -> None:
    assert get_coin_combination(value) == output


def test_check_if_value_less_than_0() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-2)

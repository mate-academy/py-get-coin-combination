import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (101, [1, 0, 0, 4])
    ]
)
def test_value_should_be_ok(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result, \
        f"For {cents} cents must return {result}"


def test_raising_error_correctly() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")

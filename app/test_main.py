from app.main import get_coin_combination
import pytest


def test_should_raise_typeerror() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15 cents")


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (4555, [0, 1, 0, 182])
    ]
)
def test_should_return_expected(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected, \
        "Expected result is incorrect"

from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_code_work(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("3")


def test_wrong_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-3)

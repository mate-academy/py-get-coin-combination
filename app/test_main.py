import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (16, [1, 1, 1, 0]),
        (41, [1, 1, 1, 1]),
        (9222241469, [4, 1, 1, 368889658])
    ],
    ids=[
        "test zero cents",
        "test pennies",
        "test nickels",
        "test dimes",
        "test quarters",
        "test huge cents number"
    ]
)
def test_can_sum(cents: int, result: list[int]) -> None:
    assert (get_coin_combination(cents) == result),\
        f"Result of func for cents={cents} and should be equal to {result}"


def test_raise_typeerror_if_not_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("100")


def test_raise_valueerror_negative_cents() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(
        value: int,
        result: list
) -> None:
    assert get_coin_combination(value) == result


@pytest.mark.parametrize(
    "value, result",
    [
        ("6", TypeError),
        (None, TypeError),
    ]
)
def test_get_coin_combination_error(
        value: int,
        result: list
) -> None:
    with pytest.raises(result):
        get_coin_combination(value)

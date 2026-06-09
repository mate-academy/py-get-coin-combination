import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        ({1, 2, 3}, TypeError),
        ("23", TypeError),
    ]
)
def test_get_coin_combination_raises_exceptions(
        cents: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

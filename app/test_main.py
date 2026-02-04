from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (15, [0, 1, 1, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (10000, [0, 0, 0, 400]),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_should_raise_error_with_negative_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_should_raise_error_if_length_list_not_four() -> None:
    result = get_coin_combination(3)
    assert len(result) == 4

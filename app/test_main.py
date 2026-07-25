import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_return_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_should_raise_error_for_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("coins")

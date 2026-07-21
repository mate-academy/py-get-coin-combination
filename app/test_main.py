import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [
    "1",
    ([10]),
    ({"cents": 15})
])
def test_should_raise_error_if_cents_is_not_correct_type(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

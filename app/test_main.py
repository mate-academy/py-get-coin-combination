import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test should accept 0 cents"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="test should accept 1 cent and return 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="test should accept 6 cents and return 1 penny + 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="test should accept 17 cents and return 2 + 1 + 1"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="test should accept 50 cents and return 2 quarters"
        ),
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected


def test_get_coin_combination_should_raise_type_error_for_str_input() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("50")

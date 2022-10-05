import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            0,
            [0] * 4,
            id="should return [0, 0, 0, 0] if there are no cents"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return [1, 0, 0, 0] if there is 1 cent"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return [1, 1, 0, 0] if there are 6 cents"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return [2, 1, 1, 0] if there are 17 cents"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return [0, 0, 0, 2] if there are 50 cents"
        ),
    ]
)
def test_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected

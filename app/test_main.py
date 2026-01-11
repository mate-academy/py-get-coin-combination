import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zeros when cents zero"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1, 0, 0, 0 when cents 1"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1, 1, 0, 0 when cents 6"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 2, 1, 1, 0 when cents 17"
        ),
        pytest.param(
            50,
            [0, 0, 0, 2],
            id="should return 0, 0, 0, 1 when cents 50"
        ),
        pytest.param(
            999,
            [4, 0, 2, 39],
            id="extra large"
        )
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

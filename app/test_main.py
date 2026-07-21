import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return list [1, 0, 0, 0]"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return list [1, 1, 0, 0]"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should return list [2, 1, 1, 0]"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="should return list [0, 0, 0, 2]"
        ),
    ]
)
def test_get_coin_combination(cents: int, expected: int) -> None:
    assert get_coin_combination(cents) == expected

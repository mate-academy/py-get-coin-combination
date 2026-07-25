import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_combination",
    [
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(5, [0, 1, 0, 0]),
        pytest.param(10, [0, 0, 1, 0]),
        pytest.param(25, [0, 0, 0, 1]),
        pytest.param(41, [1, 1, 1, 1]),
        pytest.param(82, [2, 1, 0, 3]),
    ],
)
def test_getting_coin_combination_correctly(
    cents: int, expected_combination: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_combination

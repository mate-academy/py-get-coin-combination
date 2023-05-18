import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    pytest.param(17, [2, 1, 1, 0], id="should return different coins"),
    pytest.param(0, [0, 0, 0, 0], id="argument should be positive"),
    pytest.param(5, [0, 1, 0, 0]),
    pytest.param(50, [0, 0, 0, 2]),
    pytest.param(1, [1, 0, 0, 0]),
    pytest.param(10, [0, 0, 1, 0])
])
def test_should_return_correct_result(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

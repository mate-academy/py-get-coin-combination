import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    pytest.param(0, [0, 0, 0, 0], id="0 cents"),
    pytest.param(1, [1, 0, 0, 0], id="1 cent"),
])
def test_small_values(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    pytest.param(6, [1, 1, 0, 0], id="6 cents"),
    pytest.param(17, [2, 1, 1, 0], id="17 cents"),
])
def test_multiple_coin_types(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    pytest.param(75, [0, 0, 0, 3], id="75 cents"),
])
def test_single_coin_type(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    pytest.param(41, [1, 1, 1, 1], id="41 cents"),
])
def test_all_coin_types(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents, expected", [
    pytest.param(176, [1, 0, 0, 7], id="176 cents"),
])
def test_large_values(cents: int, expected: list[int]) -> None:
    assert get_coin_combination(cents) == expected

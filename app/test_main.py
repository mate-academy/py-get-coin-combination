from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents, expected_values", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])])
def test_basic_examples(cents: int, expected_values: list) -> None:
    assert get_coin_combination(cents) == expected_values


def test_negative_values() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


@pytest.mark.parametrize("cents", ["one", 2.53, True]
                         )
def test_invalid_types(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


def test_boundaries() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]
    assert get_coin_combination(1) == [1, 0, 0, 0]
    assert get_coin_combination(24) == [4, 0, 2, 0]
    assert get_coin_combination(25) == [0, 0, 0, 1]

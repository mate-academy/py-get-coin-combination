import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("value,expected_results", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (50, [0, 0, 0, 2]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (24, [4, 0, 2, 0]),
    (1000, [0, 0, 0, 40]),
    (99, [4, 0, 2, 3])
])
def tests(value: int, expected_results: list) -> None:
    assert get_coin_combination(value) == expected_results


def test_negative() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-3)


def test_not_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(3.45)

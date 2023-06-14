import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("value,expected",
                         [(1, [1, 0, 0, 0]),
                          (6, [1, 1, 0, 0]),
                          (17, [2, 1, 1, 0]),
                          (50, [0, 0, 0, 2])])
def test_base_res(value: int, expected: list) -> None:
    assert get_coin_combination(value) == expected


def test_zero_res() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]

import pytest

import app.main as main


@pytest.mark.parametrize(
    "cents, expected",
    [
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert main.get_coin_combination(cents) == expected


def test_get_coin_combination_negative() -> None:
    with pytest.raises(ValueError):
        main.get_coin_combination(-1)


def test_check_if_number_is_string() -> None:
    with pytest.raises(TypeError):
        main.get_coin_combination("1")

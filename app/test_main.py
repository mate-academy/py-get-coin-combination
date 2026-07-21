import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (11, [1, 0, 1, 0]),
    (17, [2, 1, 1, 0]),
    (25, [0, 0, 0, 1]),
    (26, [1, 0, 0, 1]),
    (50, [0, 0, 0, 2]),
    (6**10, [1, 0, 0, 2418647]),
])
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_should_truncate_float_values() -> None:
    assert get_coin_combination(15.9) == [0, 1, 1, 0]


def test_negative_numbers() -> None:
    assert get_coin_combination(-15) == [0, 0, 0, 0]


@pytest.mark.parametrize("bad_cent, expected_exception", [
    ("abc", TypeError),      # Рядок неможливо перетворити на int
    (None, TypeError),       # None викликає TypeError при int(None)
    ([], TypeError),         # Список викликає TypeError
    (object(), TypeError),   # Об'єкт викликає TypeError
])
def test_should_raise_error_on_invalid_types(bad_cent: int,
                                             expected_exception: list) -> None:
    with pytest.raises(expected_exception):
        get_coin_combination(bad_cent)

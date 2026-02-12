import pytest
from app.main import get_coin_combination


def test_function_always_returns_list_of_length_4() -> None:
    result = get_coin_combination(37)
    assert isinstance(result, list)
    assert len(result) == 4


@pytest.mark.parametrize("cents, result", [
    (0, [0, 0, 0, 0]),
    (1, [1, 0, 0, 0]),
    (4, [4, 0, 0, 0]),
    (5, [0, 1, 0, 0]),
    (6, [1, 1, 0, 0]),
    (9, [4, 1, 0, 0]),
    (10, [0, 0, 1, 0]),
    (16, [1, 1, 1, 0]),
    (17, [2, 1, 1, 0]),
    (24, [4, 0, 2, 0]),
    (25, [0, 0, 0, 1]),
    (41, [1, 1, 1, 1]),
    (99, [4, 0, 2, 3]),
    (100, [0, 0, 0, 4])
])
def test_get_coin_combination_valid_inputs_return_expected(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize("cents, exception", [
    pytest.param(-1, ValueError, id="non-negative integer"),
    pytest.param("a", TypeError, id="value must be an integer"),
    pytest.param(1.5, TypeError, id="value must be an integer")
])
def test_get_coin_combination_raises_error(
        cents: object,
        exception: object
) -> None:
    with pytest.raises(exception):
        get_coin_combination(cents)

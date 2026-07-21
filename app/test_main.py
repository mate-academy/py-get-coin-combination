import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents", [1.5])
def test_should_return_list_for_float(cents: int) -> None:
    result = get_coin_combination(cents)
    assert isinstance(result, list)
    assert all(isinstance(x, (int, float)) for x in result)


@pytest.mark.parametrize("cents", ["10", None, [10]])
def test_should_raise_error_for_invalid_types(cents: int) -> None:
    with pytest.raises(Exception):
        get_coin_combination(cents)


def test_should_return_combination_of_different_coins() -> None:
    result = get_coin_combination(17)
    assert result == [2, 1, 1, 0]

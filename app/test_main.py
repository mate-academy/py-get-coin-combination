import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(0, [0, 0, 0, 0], id="should return list with zeros if cents is 0"),
        pytest.param(1, [1, 0, 0, 0], id="should return list with 1 penny if cents is 1"),
        pytest.param(7, [2, 1, 0, 0], id="should return list with 2 pennies 1 nickel if cents is 7"),
        pytest.param(24, [4, 0, 2, 0], id="should return list with 2 dimes 4 pennies if cents is 24"),
        pytest.param(50, [0, 0, 0, 2], id="should return list with 2 quarters if cents is 50"),
        pytest.param(5568, [3, 1, 1, 222], id="should return list with 222 quarters 1 dime 1 nickel 3 pennies if cents is 5568"),
    ]
)
def test_with_different_params(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


def test_should_return_list_with_different_types_of_coins() -> None:
    assert get_coin_combination(87)[3] != get_coin_combination(87)[2] != get_coin_combination(87)[1] != get_coin_combination(87)[0]


def test_sum_of_coins_value_is_equal_to_cents() -> None:
    assert get_coin_combination(41)[3] * 25 + get_coin_combination(41)[2] * 10 + get_coin_combination(41)[1] * 5 + get_coin_combination(41)[0] == 41


def test_should_return_list_type() -> None:
    assert isinstance(get_coin_combination(1), list)


def test_should_return_collection_with_four_elements() -> None:
    assert len(get_coin_combination(1)) == 4


@pytest.mark.parametrize(
    "cents, exception",
    [
        pytest.param("4", TypeError, id="should raise TypeError if cents is string type"),
        pytest.param(None, TypeError, id="should raise TypeError if cents is None"),
    ]
)
def test_should_raise_correct_error(cents: str | None, exception: type[Exception]) -> None:
    with pytest.raises(exception):
        get_coin_combination(cents)


def test_previous_params_should_not_interfere() -> None:
    result_one = get_coin_combination(33)
    result_two = get_coin_combination(143)
    result_three = get_coin_combination(33)
    assert result_one == result_three != result_two

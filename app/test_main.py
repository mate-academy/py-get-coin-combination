import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param(
            35,
            id="function should return list"
        )
    ]
)
def test_should_return_list(cents: int) -> None:
    assert isinstance(get_coin_combination(cents), list)


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param(
            17,
            id="function should return list of length = 4"
        )
    ]
)
def test_should_return_list_of_length_4(cents: int) -> None:
    assert len(get_coin_combination(cents)) == 4


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param(
            17,
            id="function should return list of non-negative integers"
        )
    ]
)
def test_should_return_list_of_non_negative_integers(cents: int) -> None:
    for number in get_coin_combination(cents):
        assert number >= 0 and isinstance(number, int)


@pytest.mark.parametrize(
    "cents,coins",
    [
        pytest.param(
            26, [1, 0, 0, 1],
            id="function should return [1, 0, 0, 1] if cents = 26"
        ),
        pytest.param(
            0, [0, 0, 0, 0],
            id="function should return [0, 0, 0, 0] if cents = 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="function should return [0, 0, 0, 0] if cents = 0"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="function should return [0, 1, 0, 0] if cents = 5"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="function should return [0, 0, 1, 0] if cents = 10"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="function should return [0, 0, 0, 2] if cents = 50"
        )
    ]
)
def test_should_return_correct_value(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(
            "99", TypeError,
            id="should raise TypeError if cents  not integer"
        )
    ]
)
def test_should_raising_errors_correctly(
        cents: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

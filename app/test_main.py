import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_return_exact_result(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_should_return_list_of_four_integers() -> None:
    result = get_coin_combination(5)

    assert len(result) == 4
    assert all(isinstance(coin, int) for coin in result)


def test_should_raise_error_if_value_is_str() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("1")

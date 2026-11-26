import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (50, [0, 0, 0, 2])
    ]
)
def test_the_function_works_correctly(
        cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result


def test_if_the_function_raises_exception_if_cents_is_negative() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-2)


@pytest.mark.parametrize(
    "cents",
    [
        "one",
        5.5,
        True,
        False
    ]
)
def test_if_the_function_raises_exception_if_cents_is_not_int(
        cents: str | int | float | bool
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


"""
1. Zwykły test z poprawną ilością cents i czy funkcja działa
2. Co się dzieje jeśli cents jest ujemne? - ValueError
3. Co się dzieje jeśli cents nie jest integerem? - TypeError

1. 0, 1, 4, 5, 6, 9, 10, 17, 24, 25, 50
"""

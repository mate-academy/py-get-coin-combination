import pytest


from app.main import get_coin_combination


def test_correct_error_raised() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("100")


def test_output_list_of_int() -> None:
    result = isinstance(get_coin_combination(333)[0], int)
    assert (
        result is True
    ), "Output should be integer"


@pytest.mark.parametrize(
    "coins, result",
    [
        (0, [0, 0, 0, 0]),
        (-100, [0, 0, 0, -4]),
        (17, [2, 1, 1, 0]),
        (3333333, [3, 1, 0, 133333])
    ],
    ids=[
        "Zero has to return all zeros",
        "Negative input can not be processed correctly",
        "Return is list with integers",
        "large numbers can be processed"
    ]
)
def test_get_coin_combinations(coins: int, result: list) -> None:
    assert (
        get_coin_combination(coins) == result
    ), f"{coins} has to produce {result}"

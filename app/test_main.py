import pytest


from app.main import get_coin_combination


def test_should_return_list() -> None:
    assert isinstance(get_coin_combination(1), list)


def test_should_return_length_is_4() -> None:
    assert len(get_coin_combination(1)) == 4


@pytest.mark.parametrize(
    "coins,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_results(coins: int, result: list) -> None:
    assert get_coin_combination(coins) == result

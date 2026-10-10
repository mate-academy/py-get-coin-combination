import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    (
        [0, [0, 0, 0, 0]],
        [1, [1, 0, 0, 0]],
        [5, [0, 1, 0, 0]],
        [6, [1, 1, 0, 0]],
        [10, [0, 0, 1, 0]],
        [16, [1, 1, 1, 0]],
        [17, [2, 1, 1, 0]],
        [25, [0, 0, 0, 1]],
        [41, [1, 1, 1, 1]],
        [50, [0, 0, 0, 2]],
        [91, [1, 1, 1, 3]]
    )
)
def test_core_get_coin_combination(
    cents: int, result: list[int]
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents,result",
    (
        [6, [1, 1, 0, 0]],
        [15, [0, 1, 1, 0]],
        [16, [1, 1, 1, 0]],
        [17, [2, 1, 1, 0]],
        [41, [1, 1, 1, 1]],
        [48, [3, 0, 2, 1]],
        [91, [1, 1, 1, 3]]
    )
)
def test_if_has_different_types_of_coins(
    cents: int, result: list[int]
) -> None:
    actual = get_coin_combination(cents)
    positive_values = [
        number_of_coins for number_of_coins in actual if number_of_coins > 0
    ]
    assert len(positive_values) >= 2

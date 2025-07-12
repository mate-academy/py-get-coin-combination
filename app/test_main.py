import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "returns zero",
        "returns one",
        "returns one nickels",
        "returns one dimes",
        "returns two quarters"
    ],
)
def test_coins_yard(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


def test_on_len_result_list() -> None:
    assert len(get_coin_combination(6)) == 4

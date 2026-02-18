import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected


def test_get_sum() -> None:
    assert sum([get_coin_combination(73)[0] * 1,
               get_coin_combination(73)[1] * 5,
               get_coin_combination(73)[2] * 10,
               get_coin_combination(73)[3] * 25]) == 73


def test_get_result_len() -> None:
    assert len(get_coin_combination(73)) == 4

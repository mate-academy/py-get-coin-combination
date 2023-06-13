import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, 1),
        (3, 3),
        (4, 4),
        (5, 0)
    ]
)
def test_number_of_pennies_always_less_than_5(cents: int, result: int) -> None:
    assert get_coin_combination(cents)[0] == result


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, 0),
        (5, 1),
        (9, 1),
        (10, 0),
        (15, 1)
    ]
)
def test_number_of_nickels_always_less_than_2(cents: int,
                                               result: int) -> None:
    assert get_coin_combination(cents)[1] == result


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, 0),
        (10, 1),
        (20, 2),
        (30, 0),
        (35, 1)
    ]
)
def test_number_of_dimes_always_less_than_3(cents: int, result: int) -> None:
    assert get_coin_combination(cents)[2] == result


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, False),
        (25, True),
        (24, False),
        (30, True),
        (100, True)
    ]
)
def test_should_always_be_quarter_if_cent_grater_24(cents: int,
                                                    result: int) -> None:
    assert (get_coin_combination(cents)[3] >= 1) == result

import pytest

from app.main import get_coin_combination


def test_should_return_list() -> None:
    goals = get_coin_combination(5)
    assert isinstance(goals, list)


def test_should_return_list_of_given_length() -> None:
    goals = get_coin_combination(5)
    assert len(goals) == 4


@pytest.mark.parametrize(
    "cents, result, test_id",
    [
        # (-14, [0, 0, 0, 0],
        #  "Negative values should return zeros"),
        (0, [0, 0, 0, 0],
         "Zero cents should return zeros"),
        (1, [1, 0, 0, 0],
         "One cent should return 1 penny"),
        (6, [1, 1, 0, 0],
         "Six cents should return 1 penny + 1 nickel"),
        (17, [2, 1, 1, 0],
         "One cent should return 2 pennies + 1 nickel + 1 dime"),
        (50, [0, 0, 0, 2],
         "One cent should return 2 quarters"),
    ],
)
def test_errors_for_type_values(
        cents: int,
        result: list[int],
        test_id: str
) -> None:
    assert get_coin_combination(cents) == result

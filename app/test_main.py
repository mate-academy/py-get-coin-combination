import pytest
from typing import Any

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,specific_coins",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="for 0 coins should return 0 specific coins"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="for coins < 5 should return only pennies"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="for 5 cons should return only nickels"
        ),
        pytest.param(
            8,
            [3, 1, 0, 0],
            id="for coins < 10 should return only pennies and nickels"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="for 10 coins should return only dimes"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="for coins < 25 should return only pennies, nickels and dimes"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="for 25 coins should return only quarters"
        ),
        pytest.param(
            44,
            [4, 1, 1, 1],
            id="for 44 coins should return every specific coins [4, 1, 1, 1]"
        ),
        pytest.param(
            1691455,
            [0, 1, 0, 67658],
            id="for 1691455 coins should return [0, 1, 0, 67658]"
        )
    ]
)
def test_equivalence_classes_and_different_filling_list(
        cents: int,
        specific_coins: list
) -> None:
    assert get_coin_combination(cents) == specific_coins


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(
            (1,),
            TypeError,
            id="should return error with not numeric parameters"
        )
    ]
)
def test_invalid_data_type(
        cents: Any,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

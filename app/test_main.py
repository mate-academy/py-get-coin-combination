import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_amount, "
    "pennies_out, "
    "nickels_out, "
    "dimes_out, "
    "quartets_out",
    [
        (1, 1, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (4, 4, 0, 0, 0),
        (5, 0, 1, 0, 0),
        (9, 4, 1, 0, 0),
        (10, 0, 0, 1, 0),
        (16, 1, 1, 1, 0),
        (19, 4, 1, 1, 0),
        (25, 0, 0, 0, 1),
        (2500, 0, 0, 0, 100),
        (49, 4, 0, 2, 1)
    ]
)
def test_valid_result(
        cents_amount: int,
        pennies_out: int,
        nickels_out: int,
        dimes_out: int,
        quartets_out: int
) -> None:
    assert (get_coin_combination(cents_amount)
            == [pennies_out,
                nickels_out,
                dimes_out,
                quartets_out])

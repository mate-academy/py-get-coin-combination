import pytest

from app.main import get_coin_combination

@pytest.mark.parametrize(
    "cents, expected", [
        pytest.param(1, [1, 0, 0, 0], id="one_penny_one_cent"),
        pytest.param(6, [1, 1, 0, 0], id="one_nickel_five_cents"),
        pytest.param(16, [1, 1, 1, 0], id="one_dime_ten_cents"),
        pytest.param(41, [1, 1, 1, 1], id="one_quarter_twentyfive_cents")
    ]
)

def test_get_coin_combination(

        cents: int,
        expected: list

) -> None:

    assert get_coin_combination(cents) == expected

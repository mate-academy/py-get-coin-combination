import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero input returns list consist "
                                         "of zeros"),
        pytest.param(2, [2, 0, 0, 0], id="testing amount of pennies"),
        pytest.param(7, [2, 1, 0, 0], id="testing pennies and nickels"),
        pytest.param(18, [3, 1, 1, 0], id="testing pennies, nickels "
                                          "and dimes"),
        pytest.param(150, [0, 0, 0, 6], id="testing big value for quarters")
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result

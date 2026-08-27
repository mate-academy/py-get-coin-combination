import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 penny"),
        pytest.param(6, [1, 1, 0, 0], id="1 penny + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
        pytest.param(0, [0, 0, 0, 0], id="zero cents"),
        pytest.param(479, [4, 0, 0, 19], id="big num if cents"),
        pytest.param(10_000_000, [0, 0, 0, 400000],
                     id="very big num of cents"),
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result

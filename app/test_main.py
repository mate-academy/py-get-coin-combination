import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    (
        pytest.param(0, [0, 0, 0, 0], id="Zero"),
        pytest.param(4, [4, 0, 0, 0], id="Pennie higher bound"),
        pytest.param(5, [0, 1, 0, 0], id="Nickel lower bound"),
        pytest.param(9, [4, 1, 0, 0], id="Nickel higher bound"),
        pytest.param(10, [0, 0, 1, 0], id="Dime lower bound"),
        pytest.param(19, [4, 1, 1, 0], id="Dime higher bound"),
        pytest.param(25, [0, 0, 0, 1], id="Quarter lower bound"),
        pytest.param(44, [4, 1, 1, 1], id="All fields count"),
        pytest.param(1019, [4, 1, 1, 40], id="Huge value")
    )
)
def test_get_coin_combination(amount: int, expected: list) -> None:

    assert get_coin_combination(amount) == expected

import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="List should contain four zeros"),
        pytest.param(1, [1, 0, 0, 0], id="List should contain one penny"),
        pytest.param(5, [0, 1, 0, 0], id="List should contain one nickel"),
        pytest.param(10, [0, 0, 1, 0], id="List should contain one dime"),
        pytest.param(25, [0, 0, 0, 1], id="List should contain one quarter"),
        pytest.param(42, [2, 1, 1, 1], id="List should contain all types"),
    ]
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

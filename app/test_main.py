import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0],
                     id="should return 1 cent"),
        pytest.param(5, [0, 1, 0, 0],
                     id="should return 1 nickel"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should return 1 cent and 1 nickel"),
        pytest.param(10, [0, 0, 1, 0],
                     id="should return only dime"),
        pytest.param(17, [2, 1, 1, 0],
                     id="should return cents, dime and nickel"),
        pytest.param(50, [0, 0, 0, 2],
                     id="should return only quarters"),
        pytest.param(94, [4, 1, 1, 3],
                     id="should return cents, nickel, dime and quarters"),
        pytest.param(0, [0, 0, 0, 0],
                     id="should return all 0 when initial valur is 0")
    ]
)
def test_convert_correctly(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

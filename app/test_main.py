import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),  # 1 penny
        (6, [1, 1, 0, 0]),  # 1 penny + 1 nickel
        (17, [2, 1, 1, 0]),  # 2 pennies + 1 nickel + 1 dime
        (50, [0, 0, 0, 2]),
        (1024, [4, 0, 2, 40])
    ]
)
def test_get_coin_combination(cents: int, result: list[int]) -> None:
    calculated_result = get_coin_combination(cents)
    assert (
        calculated_result == result
    ), (f"Failed: calculation incorrect, cents: {cents}, "
        f"result: {calculated_result}")


@pytest.mark.parametrize(
    "cents",
    [
        ("99"),
        ([25,])
    ]
)
def test_with_invalid_types(cents: str | list) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

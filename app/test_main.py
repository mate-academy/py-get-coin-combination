import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "penny,nickel,dime,quarters,cents",
    [
        (1, 0, 0, 0, 1),
        (1, 1, 0, 0, 6),
        (2, 1, 1, 0, 17),
        (0, 0, 0, 2, 50)
    ]
)
def test_different_combinations(
        penny: int,
        nickel: int,
        dime: int,
        quarters: int,
        cents: int
) -> None:
    assert get_coin_combination(cents) == [
        penny,
        nickel,
        dime,
        quarters
    ]

def test_cents_wrong_type_str() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15")
    with pytest.raises(TypeError):
        get_coin_combination(25.5)

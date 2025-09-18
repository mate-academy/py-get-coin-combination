from app.main import get_coin_combination
import pytest


@pytest.fixture
def coins() -> list:
    return [0, 0, 0, 0]  # [penny, nickel, dime, quarter]


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2]),
]
                         )
def test_get_coin_combination(cents: int, expected: list, coins: list):
    assert get_coin_combination(cents) == expected


def test_cents_only_integer() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("0")
    with pytest.raises(TypeError):
        get_coin_combination(None)
    with pytest.raises(TypeError):
        get_coin_combination(2.5)


def test_return_type_and_structure() -> None:
    result = get_coin_combination(28)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)

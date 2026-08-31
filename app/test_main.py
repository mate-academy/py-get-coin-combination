import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "values,cents",
    [
        ([1, 0, 0, 0], 1),
        ([1, 1, 0, 0], 6),
        ([2, 1, 1, 0], 17),
        ([0, 0, 0, 2], 50),
        ([4, 0, 2, 3], 99),
        ([0, 0, 0, 0], 0)
    ]
)
def test_different_combinations(
        values: list[int],
        cents: int
) -> None:
    assert get_coin_combination(cents) == values


def test_cents_wrong_type_str() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15")

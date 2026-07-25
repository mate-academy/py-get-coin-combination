import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_combination",
    [
        (67, [2, 1, 1, 2]),
        (2, [2, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (20, [0, 0, 2, 0]),
        (51, [1, 0, 0, 2]),
        (0, [0, 0, 0, 0]),

    ]
)
def test_can_calculate_coin_combination_correctly(
        cents: int,
        expected_combination: list
) -> None:
    assert get_coin_combination(cents) == expected_combination


def test_should_raise_errors_correctly() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("5")

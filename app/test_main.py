import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (66, [1, 1, 1, 2])
    ]
)
def test_func_should_return_correct_values_for_boundary_conditions(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected


def test_should_raise_right_error_in_wrong_input_case() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15")

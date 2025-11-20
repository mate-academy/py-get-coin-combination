import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents", [
        ("1"),
        (6.45),
        ([17]),
        ({50}),
    ]
)
def test_wrong_type_input(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents", [
        (-1),
        (-6),
        (-17),
        (-50),
    ]
)
def test_negative_input(cents: int) -> None:
    with pytest.raises(ValueError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents, result", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_correct_values_result_logic(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

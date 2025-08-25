from app.main import get_coin_combination
import pytest


def test_should_input_correct_type_varieble() -> None:
    cents = "34"
    with pytest.raises(TypeError):
        get_coin_combination(cents=cents)


def test_should_input_only_positive_value() -> None:
    cents = -25
    with pytest.raises(ValueError):
        get_coin_combination(cents=cents)


def test_should_return_list_with_integers() -> None:
    cents = 34
    result = get_coin_combination(cents=cents)
    assert (isinstance(result, list) and isinstance(result[0], int) and isinstance(result[1], int)
            and isinstance(result[2], int) and isinstance(result[3], int))


@pytest.mark.parametrize(
    "cents,result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (1000, [0, 0, 0, 40])
    ]
)
def test_correct_work_of_func(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents=cents) == result

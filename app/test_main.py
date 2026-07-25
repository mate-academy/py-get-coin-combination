import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "initial_amount,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (17, [2, 1, 1, 0]),
        (0, [0, 0, 0, 0]),
        (1518, [3, 1, 1, 60])
    ]
)
def test_should_return_list_with_correct_values(
        initial_amount: int,
        expected_result: list
) -> None:
    assert get_coin_combination(initial_amount) == expected_result


@pytest.mark.parametrize(
    "initial_amount,expected_error",
    [
        ("1", TypeError),
        ([1], TypeError)
    ]
)
def test_should_raise_expected_error(
        initial_amount: int,
        expected_error: TypeError
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(initial_amount)

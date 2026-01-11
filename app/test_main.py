import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount_in_cents,list_of_values",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        pytest.param(
            3421,
            [1, 0, 2, 136],
            id="should work with large 'amount_in_cents'"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return zeros when 'amount_in_cents' is 0"
        )
    ]
)
def test_should_return_list_with_correct_values(
        amount_in_cents: int,
        list_of_values: list
) -> None:
    assert get_coin_combination(amount_in_cents) == list_of_values


@pytest.mark.parametrize(
    "amount_of_cents",
    [
        ("50", TypeError)
    ]
)
def test_should_raise_error_when_amount_of_incorrect_data_type(
        amount_of_cents: int
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(amount_of_cents)

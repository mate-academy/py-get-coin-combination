import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result_list",
    [
        pytest.param(
            8, [3, 1, 0, 0],
            id="return positive coins when given cents more than 0"
        ),
        pytest.param(
            0, [0, 0, 0, 0],
            id="return 0 when give zero cents"
        ),
        pytest.param(
            -38, [2, 0, 1, -2],
            id="return negative coins when given cents is negative number"
        )
    ]
)
def test_get_coin_combination_correctly(cents: int, result_list: list) -> None:
    assert get_coin_combination(cents) == result_list


@pytest.mark.parametrize(
    "cents, excepted_error",
    [
        pytest.param(
            [], TypeError,
            id="should raise error when incorrect type"
        )
    ]
)
def test_raise_error_correctly(cents, excepted_error) -> None:
    with pytest.raises(excepted_error):
        get_coin_combination(cents)

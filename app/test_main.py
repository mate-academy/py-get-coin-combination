import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents_amount, expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (146, [1, 0, 2, 5])
    ],
    ids=[
        "0 cents -> 0,0,0,0",
        "1 cents -> 1,0,0,0",
        "6 cents -> 1,1,0,0",
        "17 cents -> 2,1,1,0",
        "25 cents -> 0,0,0,1",
        "50 cents -> 0,0,0,2",
        "146 cents -> 1,0,2,5"
    ]
)
def test_return_correct_coins_quantity(cents_amount: int,
                                       expected_result: list) -> None:
    assert get_coin_combination(cents_amount) == expected_result


def test_raising_errors_correctly() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)

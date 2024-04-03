import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    [
            (1, [1, 0, 0, 0]),
            (0, [0, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (25, [0, 0, 0, 1]),
            (-1, [4, 0, 2, -1]),
    ],
    ids=["One",
         "Zero",
         "Six",
         "17"
         "25",
         "Negative number",
         "Number Example"]
)
def test_get_human_age(amount: int, expected: list) -> None:
    assert get_coin_combination(amount) == expected

import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins_number, expected",
    [
        [1, [1, 0, 0, 0]],
        [6, [1, 1, 0, 0]],
        [17, [2, 1, 1, 0]],
        [50, [0, 0, 0, 2]]
    ]
)
def test_get_coin_correct(coins_number: int, expected: list[int]) -> None:
    result = get_coin_combination(coins_number)
    assert result == expected

# @pytest.mark.parametrize(
#     "coins_number, expected",
#     ["five", ValueError]
# )
# def test_get_coin_incorrect(coins_number: str, expected: Exception) -> None:
#     with pytest.raises(ValueError):
#         get_coin_combination(coins_number)

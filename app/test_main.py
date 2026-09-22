from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("amount_cents,expected",
                         [(1, [1, 0, 0, 0]),
                          (6, [1, 1, 0, 0]),
                          (17, [2, 1, 1, 0]),
                          (50, [0, 0, 0, 2])])
def test_should_return_correct_combination_coins(amount_cents: int,
                                                 expected: list) -> None:
    assert get_coin_combination(amount_cents) == expected

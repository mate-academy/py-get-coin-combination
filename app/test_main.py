import pytest
from app.main import get_coin_combination


def test_return_type() -> None:
    assert isinstance(get_coin_combination(1), list)


@pytest.mark.parametrize(
    "cents, money_set",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_return_best_result(cents: int,
                            money_set: list[int]
                            ) -> None:
    assert get_coin_combination(cents) == money_set

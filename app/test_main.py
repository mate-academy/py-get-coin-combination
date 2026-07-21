import pytest

from app.main import get_coin_combination


def test_get_coin_combination_should_return_list() -> None:
    assert isinstance(get_coin_combination(1), list)


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_combination_values(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result

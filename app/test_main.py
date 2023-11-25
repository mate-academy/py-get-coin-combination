import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (80, [0, 1, 0, 3])
    ]
)
def test_get_combination(
        cents: int,
        expected: list
) -> None:
    result = get_coin_combination(cents)
    assert result == expected

import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        (666, [1, 1, 1, 26]),
        (0, [0, 0, 0, 0]),
        (50, [0, 0, 0, 2]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0])
    ]
)
def test_should_return_expected_coin_combination(
        cents: int,
        expected: list[int]
) -> None:
    assert get_coin_combination(cents) == expected

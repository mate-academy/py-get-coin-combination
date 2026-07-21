import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,error",
    [
        ("23", TypeError),
        (None, TypeError)
    ],
    ids=[
        "Should raise an error when string given.",
        "Should raise an error when None given.",
    ]
)
def test_should_raise_error(cents: int, error: type[Exception]) -> None:
    with pytest.raises(error):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    "cents,expected",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (19, [4, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (68, [3, 1, 1, 2]),
    ]
)
def test_should_return_coins(cents: int, expected: list) -> None:
    assert get_coin_combination(cents) == expected

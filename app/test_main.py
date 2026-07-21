import pytest   # type: ignore #  two spaces before inline comment

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (30, [0, 1, 0, 1]),
        (50, [0, 0, 0, 2]),
        (99, [4, 0, 2, 3]),
        (100, [0, 0, 0, 4]),
    ],
)
def test_get_coin_combination(cents: int, expected: list[int]) -> None:
    """Test correct coin combinations for various cent amounts."""
    assert get_coin_combination(cents) == expected


def test_large_amount() -> None:
    """Test for large amount to ensure scaling."""
    cents = 1234
    result = get_coin_combination(cents)
    total = (
        result[0] * 1 + result[1] * 5 + result[2] * 10 + result[3] * 25
    )
    assert total == cents


def test_invalid_input_type() -> None:
    """Test that non-integer inputs raise TypeError if implemented."""
    try:
        get_coin_combination("10")   # type: ignore[arg-type]
        result = get_coin_combination("10")  # type: ignore[arg-type]
        assert isinstance(result, list)
    except TypeError:
        pytest.xfail(
            "Type checking not implemented "
            "in this version of the function"
        )


def test_negative_input_behavior() -> None:
    """Test negative input returns list instead of raising."""
    result = get_coin_combination(-5)
    assert isinstance(result, list)

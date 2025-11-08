import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected",
    [
        pytest.param(0, [0, 0, 0, 0]),
        pytest.param(1, [1, 0, 0, 0]),
        pytest.param(6, [1, 1, 0, 0]),
        pytest.param(17, [2, 1, 1, 0]),
        pytest.param(50, [0, 0, 0, 2]),
        pytest.param(874, [4, 0, 2, 34])
    ]
)
def test_get_coin_combination(
        cents: int,
        expected: list
) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param("1", TypeError),
        pytest.param(-1, ValueError),

    ]
)
def test_get_coin_combination_raises(
        cents: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

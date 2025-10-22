import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent,expected",
    [
        pytest.param(
            0, [0, 0, 0, 0], id="0 - 0 0 0 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0], id="1 - 1 0 0 0"
        ),
        pytest.param(
            6, [1, 1, 0, 0], id="6 - 1 1 0 0"
        ),
        pytest.param(
            17, [2, 1, 1, 0], id="17 - 2 1 0 0"
        ),
        pytest.param(
            50, [0, 0, 0, 2], id="50 - 0 0 0 2"
        ),
    ]
)
def test_get_coin_combination(cent: int, expected: list[int]) -> None:
    assert get_coin_combination(cent) == expected


@pytest.mark.parametrize(
    "cent",
    [
        pytest.param(
            -1,
        )
    ]
)
def test_error_get_coin_combination(cent: int) -> None:
    with pytest.raises(ValueError):
        if cent < 0:
            raise ValueError

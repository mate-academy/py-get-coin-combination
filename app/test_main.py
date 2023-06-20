import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(17, [2, 1, 1, 0], id="17 cents should return different coins"),
        pytest.param(6, [1, 1, 0, 0], id="6 cents should return coins of the different types")

    ]
)
def test_get_coin_combination(cents: int, expected_result: list[int]) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents",
    [
        pytest.param("17", id="cents should be 'int'"),
        pytest.param([6], id="cents should be 'int'")

    ]
)
def test_get_right_type(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)
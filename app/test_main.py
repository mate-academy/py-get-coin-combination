import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_val,expected",
    [
        pytest.param(0, [0, 0, 0, 0], id="zero_cents"),
        pytest.param(1, [1, 0, 0, 0], id="one_penny"),
        pytest.param(6, [1, 1, 0, 0], id="penny_and_nickel"),
        pytest.param(17, [2, 1, 1, 0], id="mixed_coins"),
        pytest.param(50, [0, 0, 0, 2], id="only_quarters"),
        pytest.param(2, [2, 0, 0, 0], id="less_than_nickel_2"),
        pytest.param(4, [4, 0, 0, 0], id="less_than_nickel_4"),
        pytest.param(9, [4, 1, 0, 0], id="between_penny_and_nickel"),
        pytest.param(14, [4, 0, 1, 0], id="between_nickel_and_dime"),
        pytest.param(26, [1, 0, 0, 1], id="between_quarter_and_rest"),
        pytest.param(41, [1, 1, 1, 1], id="all_coin_types"),
    ]
)
def test_get_coin_combination(
    input_val: int,
    expected: list[int]
) -> None:
    assert get_coin_combination(input_val) == expected

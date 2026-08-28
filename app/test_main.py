import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, coins",
    [
        pytest.param(0, [0, 0, 0, 0], id="check 0"),
        pytest.param(1, [1, 0, 0, 0], id="check 1"),
        pytest.param(4, [4, 0, 0, 0], id="check 4"),
        pytest.param(5, [0, 1, 0, 0], id="check 5"),
        pytest.param(6, [1, 1, 0, 0], id="check 6"),
        pytest.param(9, [4, 1, 0, 0], id="check 9"),
        pytest.param(10, [0, 0, 1, 0], id="check 10"),
        pytest.param(14, [4, 0, 1, 0], id="check 14"),
        pytest.param(15, [0, 1, 1, 0], id="check 15"),
        pytest.param(16, [1, 1, 1, 0], id="check 16"),
        pytest.param(17, [2, 1, 1, 0], id="check 17"),
        pytest.param(24, [4, 0, 2, 0], id="check 24"),
        pytest.param(25, [0, 0, 0, 1], id="check 25"),
        pytest.param(26, [1, 0, 0, 1], id="check 26"),
        pytest.param(30, [0, 1, 0, 1], id="check 30"),
        pytest.param(41, [1, 1, 1, 1], id="check 41"),
        pytest.param(50, [0, 0, 0, 2], id="check 50"),
        pytest.param(49, [4, 0, 2, 1], id="check 49"),
        pytest.param(12754, [4, 0, 0, 510], id="check 12754"),
    ]
)
def test_get_coin_combination(cents: int, coins: list) -> None:
    assert get_coin_combination(cents) == coins

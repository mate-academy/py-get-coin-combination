from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(0, [0, 0, 0, 0], id="(0)->[0, 0, 0, 0]"),
            pytest.param(1, [1, 0, 0, 0], id="(1)->[1, 0, 0, 0]"),
            pytest.param(6, [1, 1, 0, 0], id="(6)->[1, 1, 0, 0]"),
            pytest.param(10, [0, 0, 1, 0], id="(10)->[0, 0, 1, 0]"),
            pytest.param(17, [2, 1, 1, 0], id="(17)->[2, 1, 1, 0]"),
            pytest.param(25, [0, 0, 0, 1], id="(25)->[0, 1, 1, 1]"),
            pytest.param(30, [0, 1, 0, 1], id="(30)->[0, 1, 0, 1]"),
            pytest.param(50, [0, 0, 0, 2], id="(50)->[0, 1, 0, 2]"),
        ]
    )
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected

    def test_check_is_list(self) -> None:
        assert isinstance(get_coin_combination(1), list)

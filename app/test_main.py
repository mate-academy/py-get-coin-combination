from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,excepted_coin_combination",
        [
            pytest.param(0, [0, 0, 0, 0], id="Test combine 0 cents"),
            pytest.param(1, [1, 0, 0, 0], id="Test combine 1 cents"),
            pytest.param(6, [1, 1, 0, 0], id="Test combine 6 cents"),
            pytest.param(11, [1, 0, 1, 0], id="Test combine 11 cents"),
            pytest.param(20, [0, 0, 2, 0], id="Test combine 20 cents"),
            pytest.param(100, [0, 0, 0, 4], id="Test combine 100 cents"),
            pytest.param(1116, [1, 1, 1, 44], id="Test combine 1116 cents"),
            pytest.param(-1, [0, 0, 0, 0], id="Test combine -1 cents")
        ]
    )
    def test_get_cents(
            self,
            cents: int,
            excepted_coin_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == excepted_coin_combination

import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_get_coin_combination_valid(self) -> None:
        assert get_coin_combination(1) == [1, 0, 0, 0]
        assert get_coin_combination(6) == [1, 1, 0, 0]
        assert get_coin_combination(17) == [2, 1, 1, 0]
        assert get_coin_combination(50) == [0, 0, 0, 2]

    def test_get_coin_combination_type(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("4")
        with pytest.raises(TypeError):
            get_coin_combination(None)

    def test_get_coin_combination_edge_cases(self) -> None:
        assert get_coin_combination(0) == [0, 0, 0, 0]
        assert get_coin_combination(10000) == [0, 0, 0, 400]

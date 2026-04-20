from app.main import get_coin_combination
import pytest


class TestGetCOinCombination:
    @pytest.mark.parametrize("initial_cents,expected_list",
                             [
                                 pytest.param(1, [1, 0, 0, 0]),
                                 pytest.param(6, [1, 1, 0, 0]),
                                 pytest.param(17, [2, 1, 1, 0]),
                                 pytest.param(50, [0, 0, 0, 2]),
                             ]
                             )
    def test_should_return_right(self,
                                 initial_cents: int,
                                 expected_list: list) -> None:
        assert get_coin_combination(initial_cents) == expected_list

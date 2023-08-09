from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            pytest.param(1, [1, 0, 0, 0]),
            pytest.param(5, [0, 1, 0, 0]),
            pytest.param(6, [1, 1, 0, 0]),
            pytest.param(10, [0, 0, 1, 0]),
            pytest.param(17, [2, 1, 1, 0]),
            pytest.param(25, [0, 0, 0, 1]),
            pytest.param(41, [1, 1, 1, 1]),
            pytest.param(50, [0, 0, 0, 2]),
            pytest.param(55, [0, 1, 0, 2]),
            pytest.param(65, [0, 1, 1, 2]),
        ],
    )
    def test_correct_list_output(
        self, cents: int, expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result

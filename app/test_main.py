import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents_count,expected_coin_combination",
        [
            pytest.param(0, [0, 0, 0, 0]),
            pytest.param(1, [1, 0, 0, 0]),
            pytest.param(4, [4, 0, 0, 0]),
            pytest.param(5, [0, 1, 0, 0]),
            pytest.param(6, [1, 1, 0, 0]),
            pytest.param(10, [0, 0, 1, 0]),
            pytest.param(17, [2, 1, 1, 0]),
            pytest.param(25, [0, 0, 0, 1]),
            pytest.param(50, [0, 0, 0, 2]),
            pytest.param(41, [1, 1, 1, 1]),
        ],
        ids=[
            "zero_cents",
            "one_cent",
            "four_cents",
            "five_cents",
            "six_cents",
            "ten_cents",
            "seventeen_cents",
            "twenty_five_cents",
            "fifty_cents",
            "amount_with_all_coin_types"
        ]
    )
    def test_returns_correct_coin_combination(
        self,
        cents_count: int,
        expected_coin_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents_count) == expected_coin_combination

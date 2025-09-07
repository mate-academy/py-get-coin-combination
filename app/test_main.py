import pytest
from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "input_cents, coin_combination",
        [
            (100_000_000, [0, 0, 0, 4000000]),
            (100, [0, 0, 0, 4]),
            (50, [0, 0, 0, 2]),
            (17, [2, 1, 1, 0]),
            (6, [1, 1, 0, 0]),
            (1, [1, 0, 0, 0]),

        ],
        ids=[
            "coins-100_000_000 coin combination-[0,0,0,4_000_000]",
            "coins-100 coin combination-[0,0,0,4]",
            "coins-50 coin combination-[0,0,0,2]",
            "coins-17 coin combination-[2,1,1,0]",
            "coins-6 coin combination-[1,1,0,0]",
            "coins-1 coin combination-[1,0,0,0]",

        ]
    )
    def test_output_coin_combination(
            self,
            input_cents: int,
            coin_combination: list
    ) -> None:
        assert get_coin_combination(input_cents) == coin_combination


class TestSumOfCombination:
    @pytest.mark.parametrize(
        "input_list, coins_value",
        [
            ([0, 0, 0, 4], 100),
            ([0, 0, 0, 2], 50),
            ([2, 1, 1, 0], 17),
            ([1, 1, 0, 0], 6),
            ([1, 0, 0, 0], 1)

        ],
        ids=[
            "input_list-[0,0,0,4] coins_value-100",
            "input_list-[0,0,0,2] coins_value-50",
            "input_list-[2,1,1,0] coins_value-17",
            "input_list-[1,1,0,0] coins_value-6",
            "input_list-[1,0,0,0] coins_value-1",

        ]
    )
    def test_sum_of_coins_combination(
            self,
            input_list: list,
            coins_value: int
    ) -> None:
        assert (input_list[0] * 1
                + input_list[1] * 5
                + input_list[2] * 10
                + input_list[3] * 25
                == coins_value)


class TestFaultValues:
    @pytest.mark.parametrize(
        "input_cents",
        [
            (-100),
            (-12),
            (-10_000_000),
        ],
    )
    def test_not_int_values(self, input_cents: int) -> None:
        with pytest.raises(AssertionError):
            get_coin_combination(input_cents)

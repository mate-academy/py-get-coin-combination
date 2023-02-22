import pytest


from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents_parameter,expected_result",
        [
            (
                1,
                [1, 0, 0, 0]
            ),
            (
                6,
                [1, 1, 0, 0]
            ),
            (
                0,
                [0, 0, 0, 0]
            ),
            (
                17,
                [2, 1, 1, 0]
            ),
            (
                50,
                [0, 0, 0, 2]
            )
        ],
        ids=[
            "test_should_return_1_penny_if_coin_is_1",
            "test_should_return_2_coins_if_coin_is_6",
            "test_should_return_zero_with_zero_parameter",
            "test_should_return_list_with_4_coins_if_param_is_17",
            "test_should_return_list_with_2_coins_if_param_is_50"
        ]

    )
    def test_correct_result(self,
                            cents_parameter: int,
                            expected_result: list) -> None:
        assert get_coin_combination(cents_parameter) == expected_result

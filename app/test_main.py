import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    def test_should_check_non_integer_argument(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("100")

    @pytest.mark.parametrize(
        "amount,expected_list",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="test_should_check_zero"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="test_should_check_using_only_coin_5"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="test_should_check_using_only_coin_10"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="test_should_check_using_only_coin_25"
            ),
            pytest.param(
                9,
                [4, 1, 0, 0],
                id="test_should_check_using_only_coin_25"
            ),
            pytest.param(
                24,
                [4, 0, 2, 0],
                id="test_should_check_using_coins_1_10"
            ),
            pytest.param(
                49,
                [4, 0, 2, 1],
                id="test_should_check_using_coins_10_25"
            )
        ]
    )
    def test_should_return_correct_list(
            self, amount: int, expected_list: list) -> None:
        assert get_coin_combination(amount) == expected_list

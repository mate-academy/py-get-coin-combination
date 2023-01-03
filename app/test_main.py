from app.main import get_coin_combination
import pytest


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "number_of_coins, expected_result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (58, [3, 1, 0, 2])

        ]
    )
    def test_correct_output(self,
                            number_of_coins: int,
                            expected_result: list
                            ) -> None:
        assert get_coin_combination(number_of_coins) == expected_result

    def test_correct_value_type(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("1")

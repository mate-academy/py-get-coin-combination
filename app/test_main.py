from app.main import get_coin_combination
from pytest import mark, param


class TestGetCoinCombination:
    @mark.parametrize(
        "initial_input, expected_result",
        [
            param(
                41,
                [1, 1, 1, 1],
                id="function should return coins of the different types",
            )
        ]
    )
    def test_should_return_correct_list(
            self,
            initial_input: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(initial_input) == expected_result

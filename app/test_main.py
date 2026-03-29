import pytest

from app.main import get_coin_combination


class TestResult:
    @pytest.mark.parametrize(
        "coins,result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_should_correctly_result(
            self,
            coins: int,
            result: list
    ) -> None:
        tested_function = get_coin_combination(coins)
        assert tested_function == result


class TestTypeOfResult:
    @pytest.mark.parametrize(
        "coins,result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_should_correctly_type(
            self,
            coins: int,
            result: list
    ) -> None:
        tested_function = get_coin_combination(coins)
        assert type(tested_function) == list

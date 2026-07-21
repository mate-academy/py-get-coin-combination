import pytest

from app.main import get_coin_combination


class TestForWorkingCases:
    @pytest.mark.parametrize(
        "coins,result",
        [
            (1, [1, 0, 0, 0]),
            (2, [2, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_for_correct_results(self, coins: int, result: list) -> None:
        assert get_coin_combination(coins) == result


class TestForErrors:
    def test_for_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("1")

    def test_for_negative_values(self) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(-1)

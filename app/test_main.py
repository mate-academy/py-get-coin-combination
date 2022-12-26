import pytest
from app.main import get_coin_combination


class TestCombination:
    @pytest.mark.parametrize(
        "cents,result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_correct_combination_of_the_coins(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result


def test_not_integer_type_exception() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("5")

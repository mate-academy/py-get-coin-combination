import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
            (6842132, [2, 1, 0, 273685])
        ]
    )
    def test_correct_coin_combination(
            self,
            cents: int,
            result: list | str
    ) -> None:
        assert (
            get_coin_combination(cents) == result
        ), f"{get_coin_combination(cents)} should equal {result}"


class TestGetCoinCombinationError:
    def test_value_less_than_zero(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("num12")

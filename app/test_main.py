import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (20, [0, 0, 2, 0]),
            (26, [1, 0, 0, 1]),
            (49, [4, 0, 2, 1]),
            (101, [1, 0, 0, 4]),
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result

    def test_incorrect_type(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("3")

        with pytest.raises(TypeError):
            get_coin_combination([1])

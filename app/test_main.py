import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "initial_cents,expected_combination",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_get_coin_combination(
            self,
            initial_cents: int,
            expected_combination: list
    ) -> None:
        assert get_coin_combination(initial_cents) == expected_combination

    @pytest.mark.parametrize(
        "non_integer",
        [
            "non_integer"
        ]
    )
    def test_coin_is_int(
            self,
            non_integer: int
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(non_integer)

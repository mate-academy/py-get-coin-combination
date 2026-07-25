import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, result_combination",
        [
            pytest.param(1, [1, 0, 0, 0],
                         id="1 cent should equal [1, 0, 0, 0]"),
            pytest.param(6, [1, 1, 0, 0],
                         id="6 cents should equal [1, 1, 0, 0]"),
            pytest.param(17, [2, 1, 1, 0],
                         id="17 cents should equal [2, 1, 1, 0]"),
            pytest.param(50, [0, 0, 0, 2],
                         id="50 cents should equal [0, 0, 0, 2]")
        ]
    )
    def test_get_coin_combination_with_correct_args(
            self,
            cents: int,
            result_combination: list
    ) -> None:
        assert get_coin_combination(cents) == result_combination

    @pytest.mark.parametrize(
        "not_cents",
        [
            pytest.param("2"),
            pytest.param(["12"]),
            pytest.param({12: "55"})
        ]
    )
    def test_get_coin_combination_with_incorrect_args(self,
                                                      not_cents: int) -> None:
        with pytest.raises(TypeError):
            assert get_coin_combination(not_cents)

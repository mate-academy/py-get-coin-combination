from app.main import get_coin_combination
import pytest


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cent",
        [
            pytest.param(
                "8",
                id="should raise TypeError when incoming value is string"
            ),
            pytest.param(
                [13],
                id="should raise TypeError when incoming value is list"
            ),
            pytest.param(
                None,
                id="should raise TypeError when incoming value is None"
            )
        ]
    )
    def test_incoming_exceptions(
            self,
            cent: int
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cent)

    @pytest.mark.parametrize(
        "incoming_value, result",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="should not return coins"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="should return one coin each"
            ),
            pytest.param(
                9889,
                [4, 0, 1, 395],
                id="should work correctly with very large input values"
            )
        ]
    )
    def test_cent(
            self,
            incoming_value: int,
            result: list[int]
    ) -> None:
        assert (
            get_coin_combination(incoming_value) == result
        )

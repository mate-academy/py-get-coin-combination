import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents,result",
        [
            pytest.param(
                17, [2, 1, 1, 0],
                id="should return different coins")
        ]
    )
    def test_return_valid_result(
            self,
            cents: int,
            result: list
    ) -> None:
        assert get_coin_combination(cents) == result

    @pytest.mark.parametrize(
        "cents",
        [
            pytest.param(
                "12",
                id="should raise an error when argument isn't a number"),
        ]
    )
    def test_should_raise_error_if_incorrect_type(
            self,
            cents: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)

import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    def test_result_list_length_should_be_equal_to_4(self) -> None:
        assert len(get_coin_combination(0)) == 4

    @pytest.mark.parametrize(
        "coin,result_after_converting",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="0 coin should return [0, 0, 0, 0]"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 coin should return [1, 0, 0, 0]"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="6 coin should return [1, 1, 0, 0]"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 coin should return [2, 1, 1, 0]"
            ),
            pytest.param(
                41,
                [1, 1, 1, 1],
                id="41 coin should return [1, 1, 1, 1]"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="50 coin should return [0, 0, 0, 2]"
            ),
        ]
    )
    def test_coin_converting(
            self,
            coin: int,
            result_after_converting: list
    ) -> None:
        result = get_coin_combination(coin)
        assert result == result_after_converting

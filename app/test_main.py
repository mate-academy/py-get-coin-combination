import pytest
from app.main import get_coin_combination


class TestGetCoinCombinations:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(
                1,
                [1, 0, 0, 0]
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
            )
        ]
    )
    def test_get_coin_combinations(
            self,
            cents: int,
            expected: list
    ) -> None:
        assert get_coin_combination(cents) == expected

    def test_value_error(self) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(cents=-1)

    def test_coin_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("")

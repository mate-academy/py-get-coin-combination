import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents, coins_expected",
        [
            pytest.param(
                3, [3, 0, 0, 0],
                id="should take 3 penny: 3 penny expected",
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="should take 6 penny: 1 penny, 1 nickel expected",
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="should take 17 penny: 2 penny, 1 nickel, 1 dime expected",
            ),
            pytest.param(
                50, [0, 0, 0, 2],
                id="should take 50 penny: 2 quarters expected",
            )
        ]
    )
    def test_get_coin_combination(
        self,
        cents: int,
        coins_expected: list[int]
    ) -> None:
        assert get_coin_combination(cents) == coins_expected

    @pytest.mark.parametrize(
        "cents, expected_error",
        [
            pytest.param(
                "retor", TypeError,
                id="should raise error if args is str",
            )
        ]
    )
    def test_get_coin_from_str(
        self,
        cents: int,
        expected_error: type[Exception]
    ) -> None:
        with pytest.raises(TypeError):
            assert get_coin_combination(cents) == expected_error

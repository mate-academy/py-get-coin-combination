import pytest

from app.main import get_coin_combination


class TestMainClass:
    @pytest.mark.parametrize(
        "initial_cents,expected_coin_combination",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="should return 1 penny"),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="should return 1 penny, 1 nickel"),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="should return 2 pennies, 1 nickel, 1 dime"),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="should return 2 quarters")
        ]
    )
    def test_get_coin_combination(
            self,
            initial_cents: int,
            expected_coin_combination: list
    ) -> None:
        assert (get_coin_combination(initial_cents)
                == expected_coin_combination)

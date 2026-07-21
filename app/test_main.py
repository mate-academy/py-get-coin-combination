import pytest


from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents, smallest_combination",
        [
            pytest.param(
                4,
                [4, 0, 0, 0],
                id="should calculate only penny when cents < 1 nickel"
            ),
            pytest.param(
                5,
                [0, 1, 0, 0],
                id="should add nickel when it becomes possible"
            ),
            pytest.param(
                10,
                [0, 0, 1, 0],
                id="should add dime when it becomes possible"
            ),
            pytest.param(
                25,
                [0, 0, 0, 1],
                id="should add quarter when it becomes possible"
            ),
            pytest.param(
                42,
                [2, 1, 1, 1],
                id="should add all types of coins"
            )
        ]
    )
    def test_coin_combination_works_correctly(
            self,
            cents: int,
            smallest_combination: list
    ) -> None:
        assert get_coin_combination(cents) == smallest_combination

    @pytest.mark.parametrize(
        "cents, expected_error",
        [
            pytest.param(
                "some value",
                TypeError,
                id="Should raise error when cents is not integer"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cents: int,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)

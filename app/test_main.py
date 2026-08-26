import pytest

from app.main import get_coin_combination


class TestCoins:
    @pytest.mark.parametrize(
        "coins, expected_result",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (4, [4, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (9, [4, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (24, [4, 0, 2, 0]),
            (50, [0, 0, 0, 2]),
            (99, [4, 0, 2, 3]),
            (100, [0, 0, 0, 4])
        ]
    )
    def test_get_coin_combination(
            self,
            coins: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(coins) == expected_result

    @pytest.mark.parametrize(
        "coins, expected_result",
        [
            (True, [1, 0, 0, 0]),
            (9.5, [4.0, 1.0, 0.0, 0.0]),
        ]
    )
    def test_get_coin_combination_using_not_int_values(
            self,
            coins: bool | float,
            expected_result: int | float
    ) -> None:
        assert get_coin_combination(coins) == expected_result

    @pytest.mark.parametrize(
        "coins, expected_error",
        [
            ("sdfs", TypeError),
            (None, TypeError)
        ]
    )
    def test_errors(
            self,
            coins: str | None,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(coins)

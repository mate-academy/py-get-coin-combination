import pytest
from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "coin,expected_value",
        [
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (15, [0, 1, 1, 0]),
            (20, [0, 0, 2, 0]),
            (25, [0, 0, 0, 1]),
            (30, [0, 1, 0, 1]),
            (100, [0, 0, 0, 4]),
            (200, [0, 0, 0, 8]),
            (210, [0, 0, 1, 8])
        ],
        ids=[
            "checking coins with parameters: 5",
            "checking coins with parameters: 10",
            "checking coins with parameters: 15",
            "checking coins with parameters: 20",
            "checking coins with parameters: 25",
            "checking coins with parameters: 30",
            "checking coins with parameters: 100",
            "checking coins with parameters: 200",
            "checking coins with parameters: 210",
        ]
    )
    def test_get_coin_combination(
            self,
            coin: int,
            expected_value: list
    ) -> None:
        assert get_coin_combination(coin) == expected_value

    @pytest.mark.parametrize(
        "initial_coins,coin_index,expected_value",
        [
            (100, 3, 25),
            (20, 2, 10),
            (5, 1, 5),
            (4, 0, 1),
        ],
        ids=[
            "check nominal coil 25",
            "check nominal coil 10",
            "check nominal coil 5",
            "check nominal coil 1",
        ]
    )
    def test_checking_coins(
            self,
            initial_coins: int,
            coin_index: int,
            expected_value: int
    ) -> None:
        result = get_coin_combination(initial_coins)
        assert initial_coins // result[coin_index] == expected_value

    @pytest.mark.parametrize(
        "initial_coin,expected_error",
        [
            pytest.param("five", TypeError, id="coin must be int")
        ]
    )
    def test_raising_errors_correctly(
            self,
            initial_coin: str,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(initial_coin)

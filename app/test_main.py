from app.main import get_coin_combination
import pytest


class TestGetCoinCompination:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_should_return_correct_result(
        self,
        cents: int,
        expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result

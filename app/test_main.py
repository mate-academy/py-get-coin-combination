import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    @pytest.mark.parametrize(
        "cents,expected_combination",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (16, [1, 1, 1, 0]),
            (41, [1, 1, 1, 1]),
            (114, [4, 0, 1, 4]),
            (115, [0, 1, 1, 4]),
            (999, [4, 0, 2, 39])
        ]
    )
    def test_get_coin_combination_expected_result(
            self,
            cents: int,
            expected_combination: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected_combination

    def test_sum_total_must_be_equal_to_cents(self) -> None:
        values = [1, 5, 10, 25]
        coins = get_coin_combination(44)
        assert sum(values[i] * coins[i] for i in range(4)) == 44

    @pytest.mark.parametrize(
        "cents,expected_error",
        [
            ({5}, TypeError),
            ("10", TypeError)
        ]
    )
    def test_raising_test_correctly(
            self,
            cents: int,
            expected_error: [Exception]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(cents)

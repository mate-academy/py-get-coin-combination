import pytest

from app.main import get_coin_combination


class TestFetCoinCombination:
    def test_length_coins_list(self) -> None:
        assert len(get_coin_combination(1)) == 4

    def test_invalid_type_parameter(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("1")

    def test_with_zero_amountof_cents(self) -> None:
        assert get_coin_combination(0) == [0, 0, 0, 0]

    @pytest.mark.parametrize(
        "cents,expected",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ],
        ids=[
            "1 cents amount",
            "6 cents amount",
            "17 cents amount",
            "50 cents amount"
        ]
    )
    def test_expected_behavior_with_different_params(
        self,
        cents: int,
        expected: list[int]
    ) -> None:
        assert get_coin_combination(cents) == expected

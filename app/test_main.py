import pytest

from app.main import get_coin_combination


class TestCoinCombination:
    @pytest.mark.parametrize(
        "cents,expected_result",
        [
            (0, [0, 0, 0, 0]),
            (12, [2, 0, 1, 0]),
            (36, [1, 0, 1, 1]),
            (41, [1, 1, 1, 1]),
            (53, [3, 0, 0, 2])

        ]
    )
    def test_input_any_positive_number(self,
                                       cents: int,
                                       expected_result: list) -> None:
        assert get_coin_combination(cents) == expected_result

    @pytest.mark.parametrize(
        "cents",
        [
            "12",
            {"cents": 41},
            None,
            []
        ]
    )
    def test_input_unexpected_type(self, cents: any) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)

import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:
    @pytest.mark.parametrize(
        "cents, expected_list",
        [
            (0, [0, 0, 0, 0]),
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),

        ]
    )
    def test_minimal_coin_combination(
            self,
            cents: int,
            expected_list: list
    ) -> None:
        assert get_coin_combination(cents) == expected_list


def test_receives_an_incorrect_type() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("15")

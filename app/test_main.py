import pytest

from app.main import get_coin_combination


class TestGetCoinCombination:

    def test_get_coin_combination_return_list(self) -> None:
        assert isinstance(get_coin_combination(1), list)
        assert len(get_coin_combination(1)) == 4

    @pytest.mark.parametrize(
        "cents, expected",
        [
            (1, [1, 0, 0, 0]),
            (5, [0, 1, 0, 0]),
            (10, [0, 0, 1, 0]),
            (25, [0, 0, 0, 1]),
            (31, [1, 1, 0, 1]),
            (74, [4, 0, 2, 2]),
            (100, [0, 0, 0, 4]),
            (118, [3, 1, 1, 4]),
        ]
    )
    def test_get_coin_combination_true(self,
                                       cents: int,
                                       expected: list) -> None:
        assert get_coin_combination(cents) == expected, (
            f"get_coin_combination should return {expected} coins"
        )

    @pytest.mark.parametrize(
        "cents",
        [
            "12",
            [13, 4],
        ]
    )
    def test_get_coin_combination_error(self, cents: int) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)

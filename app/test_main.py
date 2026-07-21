import pytest

from app.main import get_coin_combination


class TestGetCoins:
    @pytest.mark.parametrize(
        "cents, expected",
        [
            pytest.param(1, [1, 0, 0, 0],
                         id="should return one penny if cents is equal to 1"),
            pytest.param(6, [1, 1, 0, 0],
                         id="should return amount of penny and nickel only "),
            pytest.param(17, [2, 1, 1, 0],
                         id="should return amount stated from dime, "
                            "rest for lower currencies"),
            pytest.param(50, [0, 0, 0, 2],
                         id="should return starting from quarters, "
                            "if nothing left - rest should be zero"),
            pytest.param(0, [0, 0, 0, 0], id="should return zero if no cents")
        ]
    )
    def test_get_coin_combination(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected


def test_error_occured() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("2")

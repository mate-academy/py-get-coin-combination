import pytest
from app.main import get_coin_combination


class TestChangeCoin:
    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(1, [1, 0, 0, 0], id="one cent, one penny"),
            pytest.param(6, [1, 1, 0, 0], id="6 cents, 1 penny, 1 nickel"),
            pytest.param(17, [2, 1, 1, 0], id="17 cents, 1 dime"),
            pytest.param(50, [0, 0, 0, 2], id="50 cents, 2 quarters"),
            pytest.param(0, [0, 0, 0, 0], id="0 cents, 0 changes")
        ]
    )
    def test_(self, cents: int, result: list) -> None:
        assert get_coin_combination(cents) == result

    @pytest.mark.parametrize(
        "cents",
        [
            pytest.param(-1, id="negative count cents"),
            pytest.param(-50, id="big negative count cents")
        ]
    )
    def test_negative_cents_errors(self, cents: int) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(cents)

    @pytest.mark.parametrize(
        "cents",
        [
            pytest.param("2", id="cents are string"),
            pytest.param(None, id="cents are None")
        ]
    )
    def test_type_errors(self, cents: int) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(cents)

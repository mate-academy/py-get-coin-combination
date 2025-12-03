from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, exp",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
class Test:
    def test_cents_is_non_negative(self, cents: int, exp: list) -> None:
        assert cents >= 0

    def test_coins_lenght(self, cents: int, exp: list) -> None:
        assert len(get_coin_combination(cents)) == 4


class TestEdgeCase:
    def test_cents_is_negative(self) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(-10)

    def test_cents_is_string_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("a")

    def test_cents_is_none_raises_exception(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(None)

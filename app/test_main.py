from app.main import get_coin_combination
import pytest


class TestMain:
    @pytest.mark.parametrize("cents, result", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ])
    def test_coin_combinations(self, cents: int, result: list) -> None:
        assert get_coin_combination(cents) == result

    def test_should_raise_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_coin_combination("1")
            get_coin_combination(2.5)

    def test_should_raise_value_error(self) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(-1)

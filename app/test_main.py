import pytest
from app.main import get_coin_combination


class TestClass:

    @pytest.mark.parametrize(
        "cents, result",
        [
            pytest.param(1, [1, 0, 0, 0], id="1 penny"),
            pytest.param(6, [1, 1, 0, 0],
                         id="1 penny + 1 nickel"),
            pytest.param(17, [2, 1, 1, 0],
                         id="2 pennies + 1 nickel + 1 dime"),
            pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
        ]
    )
    def test_that_should_check_all_sheet(
            self,
            cents: int,
            result: list[int]) -> None:
        actual_result = get_coin_combination(cents)
        assert actual_result == result

    def test_should_try_on_errors(self) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(-2)

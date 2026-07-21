import pytest

from app.main import get_coin_combination


class TestAddCssClass:
    @pytest.mark.parametrize(
        "incoming_cents,result_coin",
        [
            pytest.param(0, [0, 0, 0, 0], id="0 cents"),
            pytest.param(1, [1, 0, 0, 0], id="1 penny"),
            pytest.param(6, [1, 1, 0, 0], id="1 nickel + 1 penny"),
            pytest.param(15, [0, 1, 1, 0], id="1 dime + 1 nickel"),
            pytest.param(41, [1, 1, 1, 1], id="all coin types"),
            pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
            pytest.param(99, [4, 0, 2, 3], id="mixed coins 99"),
            pytest.param(24, [4, 0, 2, 0], id="24 cents edge case"),
            pytest.param(100, [0, 0, 0, 4], id="100 cents"),
        ]
    )
    def test_modify_class_correctly(self,
                                    incoming_cents: int,
                                    result_coin: list) -> None:
        assert get_coin_combination(incoming_cents) == result_coin

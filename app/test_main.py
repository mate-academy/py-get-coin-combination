import pytest
from typing import Any

from app.main import get_coin_combination


class TestCheckEdgeCases:
    @pytest.mark.parametrize(
        ("coin_input", "expected_list"),
        [
            pytest.param(
                1, [1, 0, 0, 0],
                id="test should return 1 penny when input is 1"
            ),
            pytest.param(
                6, [1, 1, 0, 0],
                id="test should return 1 penny and 1 nickel when input is 6"
            ),
            pytest.param(
                17, [2, 1, 1, 0],
                id="test should return 2110 when input is 17"
            ),
            pytest.param(
                67, [2, 1, 1, 2],
                id="test should return 2112 when input is 67"
            ),
            pytest.param(
                0, [0, 0, 0, 0],
                id="test should return 0 when input is 0"
            ),
        ]
    )
    def test_checking_edge_cases(self,
                                 coin_input: Any,
                                 expected_list: Any
                                 ) -> None:
        assert get_coin_combination(coin_input) == expected_list

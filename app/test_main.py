from app.main import get_coin_combination
import pytest


class TestData:
    @pytest.mark.parametrize(
        "init_data, expected_data",
        [
            pytest.param(
                0,
                [0, 0, 0, 0],
                id="Test Zero"
            ),
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="1 cent"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="6 cent"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="17 cent"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="50 cent"
            ),

        ]
    )
    def test_data(self,
                  init_data: int,
                  expected_data: list) -> None:
        assert get_coin_combination(init_data) == expected_data

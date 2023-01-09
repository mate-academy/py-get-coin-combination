import pytest
from app.main import get_coin_combination


class TestTrueData:
    @pytest.mark.parametrize(
        "cents,expected",
        [
            pytest.param(
                1,
                [1, 0, 0, 0],
                id="if cent is 1"
            ),
            pytest.param(
                6,
                [1, 1, 0, 0],
                id="if cents are 6"
            ),
            pytest.param(
                17,
                [2, 1, 1, 0],
                id="if cents are 17"
            ),
            pytest.param(
                50,
                [0, 0, 0, 2],
                id="if cents are 50"
            )
        ]
    )
    def test_correct_output(self, cents: int, expected: list) -> None:
        assert get_coin_combination(cents) == expected

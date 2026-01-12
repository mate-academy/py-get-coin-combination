import pytest
from app.main import get_coin_combination


class TestGetHumanAgeShouldReturnExpectedResult:
    @pytest.mark.parametrize(
        "cents, expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (10, [0, 0, 1, 0]),
            (27, [2, 0, 0, 1]),
            (66, [1, 1, 1, 2]),
            (1456, [1, 1, 0, 58])
        ]
    )
    def test_get_coin_combination(
            self,
            cents: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(cents) == expected_result

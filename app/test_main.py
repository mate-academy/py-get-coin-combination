import pytest
from typing import Type
from app.main import get_coin_combination


class TestGetCoin:
    @pytest.mark.parametrize(
        "initial_element, expected_result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2]),
        ]
    )
    def test_correctly(
            self,
            initial_element: int,
            expected_result: list
    ) -> None:
        assert get_coin_combination(initial_element) == expected_result

    @pytest.mark.parametrize(
        "initial_element, expected_error",
        [
            pytest.param("", TypeError),

        ]

    )
    def test_raising_error(
            self,
            initial_element: int,
            expected_error: Type[BaseException]
    ) -> None:
        with pytest.raises(expected_error):
            get_coin_combination(initial_element)

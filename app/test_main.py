from typing import Any


import pytest


from app.main import get_coin_combination


class TestError:
    @pytest.mark.parametrize("number",
                             [
                                 pytest.param(True,
                                              id="should raise an error "
                                                 "when cents is bool"),
                                 pytest.param(None,
                                              id="should raise an error "
                                                 "when cents is None"),
                                 pytest.param(7.9,
                                              id="should raise an error "
                                                 "when cents is float"),
                                 pytest.param("14",
                                              id="should raise an error "
                                                 "when cents is str"),
                                 pytest.param((1,),
                                              id="should raise an error "
                                                 "when cents is tuple"),
                                 pytest.param({12},
                                              id="should raise an error "
                                                 "when cents is set"),
                                 pytest.param([55],
                                              id="should raise an error "
                                                 "when cents is list"),
                                 pytest.param({"coins": 78},
                                              id="should raise an error "
                                                 "when cents is dict")
                             ])
    def test_error_when_incorrect_data(self, number: Any) -> None:
        with pytest.raises(TypeError):
            get_coin_combination(number)

    @pytest.mark.parametrize("number",
                             [
                                 -1,
                                 -10*9
                                 -1000
                             ])
    def test_error_when_value_is_negative(self, number: int) -> None:
        with pytest.raises(ValueError):
            get_coin_combination(number)


class TestValues:
    @pytest.mark.parametrize("number, result",
                             [
                                 (1, [1, 0, 0, 0]),
                                 (6, [1, 1, 0, 0]),
                                 (17, [2, 1, 1, 0]),
                                 (50, [0, 0, 0, 2]),
                                 (41, [1, 1, 1, 1]),
                             ])
    def test_is_output_correct(self, number: int, result: list) -> None:
        assert get_coin_combination(number) == result

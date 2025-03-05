from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents,result",
                         [
                             (1, [1, 0, 0, 0]),
                             (6, [1, 1, 0, 0]),
                             (17, [2, 1, 1, 0]),
                             (50, [0, 0, 0, 2]),
                         ]
                         )
def test_should_return_expected_result(cents: int,
                                       result: list) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize("values,result",
                         [
                             ([1, 5, 10, 25], 5)
                         ]
                         )
def test_value_of_coins(values: list,
                        result: int) -> None:
    assert values[3] / values[1] == result

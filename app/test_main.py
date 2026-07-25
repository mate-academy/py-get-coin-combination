from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize("cents,expected_error",
                         [
                             pytest.param(-1,
                                          ValueError,
                                          id="value cannot be negative"),
                             pytest.param("100",
                                          TypeError,
                                          id="Value must be integer"),
                         ])
def test_get_coin_combination_errors(cents: int,
                                     expected_error: type[Exception]) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)


@pytest.mark.parametrize("cents,result_list",
                         [
                             (1, [1, 0, 0, 0]),
                             (6, [1, 1, 0, 0]),
                             (17, [2, 1, 1, 0]),
                             (50, [0, 0, 0, 2]),
                         ])
def test_get_coin_combination(cents: int, result_list: list) -> None:
    assert get_coin_combination(cents) == result_list

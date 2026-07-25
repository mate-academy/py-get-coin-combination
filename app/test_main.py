from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize("cent, expected",
                         [
                             pytest.param(
                                 1, [1, 0, 0, 0],
                                 id="Cent is one"
                             ),
                             pytest.param(
                                 6, [1, 1, 0, 0],
                                 id="Cent is six"
                             ),
                             pytest.param(
                                 17, [2, 1, 1, 0],
                                 id="Cent seventeen"
                             ),
                             pytest.param(
                                 50, [0, 0, 0, 2],
                                 id="Fifty cent"
                             )
                         ])
def test_coin_function_values(cent: int, expected: list) -> None:
    assert get_coin_combination(cent) == expected


@pytest.mark.parametrize("value, expected",
                         [
                             pytest.param(
                                 None, TypeError,
                                 id="Value is None"
                             ),
                             pytest.param(
                                 "", TypeError,
                                 id="Value is not integer"
                             )
                         ])
def test_errors(value: int, expected: tuple) -> None:
    with pytest.raises(expected):
        get_coin_combination(value)

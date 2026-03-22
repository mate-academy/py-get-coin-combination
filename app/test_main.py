from typing import Type

import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize("cents, result",
                         [
                             (0, [0, 0, 0, 0]),
                             (1, [1, 0, 0, 0]),
                             (6, [1, 1, 0, 0]),
                             (17, [2, 1, 1, 0]),
                             (50, [0, 0, 0, 2])
                         ]
                         )
def test_if_coin_combination_works(cents: int,
                                   result: list[int]
                                   ) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize("cents, expected_exception",
                         [
                             ("3", TypeError),
                             ([], TypeError),
                             (-1, ValueError),
                             (-321, ValueError)

                         ]
                         )
def test_should_raise_error_for_invalid_input(
        cents: int | str | list,
        expected_exception: Type[BaseException]
) -> None:
    with pytest.raises(expected_exception):
        get_coin_combination(cents)
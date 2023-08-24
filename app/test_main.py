from app.main import get_coin_combination

import pytest


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return 4 zeros when 0 cents given"
        ),
        pytest.param(
            83,
            [3, 1, 0, 3],
            id="should place coins correctly"
        )
    ]
)
def test_should_convert_correctly(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        pytest.param(
            -20,
            ValueError,
            id="should not accept negative values"
        )
    ]
)
def test_should_raise_type_error_when_string_given(
        cents: str, expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

import pytest

from app.main import get_coin_combination


def test_cents_should_be_int_value() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("50")


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(6, [1, 1, 0, 0], id="6 cents should be "
                                         "1 nickel and 1 penny"),
        pytest.param(11, [1, 0, 1, 0], id="11 cents should be "
                                          "1 dime and 1 penny"),
        pytest.param(24, [4, 0, 2, 0], id="25 cents should be "
                                          "2 dime and 4 penny"),
        pytest.param(50, [0, 0, 0, 2], id="50 cents should be "
                                          "2 quarter")
    ]
)
def test_function_should_return_correct_combination(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result

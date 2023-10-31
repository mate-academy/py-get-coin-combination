import pytest

from app.main import get_coin_combination


def test_should_not_accept_negative_input_value() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


@pytest.mark.parametrize(
    "cents, result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_should_return_correct_combination(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"Result combination for {cents} cents must be {result}."

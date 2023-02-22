import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ],
    ids=[
        "-> 0 <- must return -> [0, 0, 0, 0] <-",
        "-> 1 <- must return -> [1, 0, 0, 0] <-",
        "-> 6 <- must return -> [1, 1, 0, 0] <-",
        "-> 17 <- must return -> [2, 1, 1, 0] <-",
        "-> 50 <- must return -> [0, 0, 0, 2] <-"
    ]
)
def test_get_coin_combination(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents) == expected_result


def test_get_coin_combination_for_non_int_values() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(get_coin_combination("2", [2], (2), {"2": 2}))

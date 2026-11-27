import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, results_list",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (9, [4, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (17, [2, 1, 1, 0]),
        (24, [4, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (50, [0, 0, 0, 2]),
        (51, [1, 0, 0, 2]),
        (1001, [1, 0, 0, 40])
    ]
)
def test_coin_combination(cents: int, results_list: list) -> None:
    assert get_coin_combination(cents) == results_list


@pytest.mark.parametrize(
    "cents",
    [
        "4",
        None,
        [],
        {}
    ]
)
def test_wrong_type(cents: str | None | list | dict):
    with pytest.raises(TypeError):
        get_coin_combination(cents)

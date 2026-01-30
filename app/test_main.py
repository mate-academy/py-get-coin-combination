from typing import Literal
import pytest
from app.main import get_coin_combination

@pytest.mark.parametrize("negative_cents", [-1, -10, -15, -25, -50, -100])
def test_negative_cents(negative_cents):
    with pytest.raises(ValueError):
        get_coin_combination(negative_cents)


@pytest.mark.parametrize(
        "cents",
        [
            "10",
             10.5,
             None,
             [1],
             {1}
        ]
)
def test_cents_input_type(cents: float | None | list[int] | set[int] | Literal['10']) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

@pytest.mark.parametrize("cents, expected", [
    (0,[0,0,0,0]),
    (1,[1, 0, 0, 0]),
    (17,[2, 1, 1, 0]),
    (50,[0,0,0,2]),
    (100,[0,0,0,4])
])
def test_should_return_correct_list(cents, expected):
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize("cents", [1,10,15,25,50,100])
def test_should_return_list_of_4_items(cents):
    assert len(get_coin_combination(cents)) == 4



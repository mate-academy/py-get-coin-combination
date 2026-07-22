import pytest
from app.main import get_coin_combination


# write your tests here
@pytest.mark.parametrize(
    "coin_value,excepted_list",
    [
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="should return only pennies"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="should return only one type of coin"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="should return only one type of coin"
        ),
        pytest.param(
            143,
            [3, 1, 1, 5],
            id="should return two or more different coin"
        )
    ]

)
def test_get_right_coin_combination(
        coin_value: int,
        excepted_list: list
) -> None:

    assert get_coin_combination(coin_value) == excepted_list

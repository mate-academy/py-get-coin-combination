from app.main import get_coin_combination
import pytest


def test_should_return_list_with_four_values() -> None:
    assert (
        isinstance(get_coin_combination(15), list)
        and len(get_coin_combination(15)) == 4
    ), "should return list with four values"


@pytest.mark.parametrize(
    "price,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (8, [3, 1, 0, 0]),
        (23, [3, 0, 2, 0]),
        (67, [2, 1, 1, 2]),
        (777, [2, 0, 0, 31])
    ],
    ids=[
        "func should return [0,0,0,0] when price equal 0",
        "func should return [4,0,0,0] when price equal 4",
        "func should return [3,1,0,0] when price equal 8",
        "func should return [3,0,2,0] when price equal 23",
        "func should return [2,1,1,2] when price equal 67",
        "func should return [2,0,0,31] when price equal 777"
    ]
)
def test_should_return_correct_values(
        price: int,
        expected_result: list
) -> None:
    assert get_coin_combination(price) == expected_result, ""

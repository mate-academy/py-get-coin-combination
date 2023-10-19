import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "num, expected_num",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_coin_combination(num: int, expected_num: list):
    assert get_coin_combination(num) == expected_num


@pytest.mark.parametrize(
    "num",
    [
        ("1"),
        ([3]),
        ({4: 1}),
    ]
)
def test_type_coin_combination(num: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(num)

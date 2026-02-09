import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "value,result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (2, [2, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (6, [1, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (11, [1, 0, 1, 0]),
        (16, [1, 1, 1, 0]),
        (20, [0, 0, 2, 0]),
        (25, [0, 0, 0, 1]),
        (26, [1, 0, 0, 1]),
        (41, [1, 1, 1, 1])
    ]
)
def test_should_return_correct_value(value: int, result: list[int]) -> None:
    assert get_coin_combination(value) == result


@pytest.mark.parametrize(
    "value,expected_error",
    [
        ("5", TypeError)
    ]
)
def test_should_return_correct_error(value: int,
                                     expected_error: Exception) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(value) == expected_error

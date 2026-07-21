from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cent,expected",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0])
    ]
)
def test_coin_combination(cent: int, expected: list) -> None:
    result = get_coin_combination(cent)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)


@pytest.mark.parametrize(
    "cent,expected",
    [
        ("10", [1, 0, 0, 0]),
        (None, [1, 1, 0, 0]),
    ],
)
def test_invalid_type_inputs(cent: int, expected: list) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cent)


@pytest.mark.parametrize(
    "cent",
    [
        (-50),
        (-13)
    ],
)
def test_negative_or_float_inputs(cent: int) -> None:
    result = get_coin_combination(cent)
    assert isinstance(result, list)
    assert len(result) == 4
    assert all(isinstance(x, int) for x in result)

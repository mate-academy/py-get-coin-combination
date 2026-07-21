import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ],
)
def test_get_coin_combination(cents: int, expected: list) -> None:
    result = get_coin_combination(cents)
    assert result == expected
    assert isinstance(result, list)
    assert len(result) == 4


@pytest.mark.parametrize(
    "bad_input",
    [
        "10",
        None,
        [1],
        {"word": 10},
    ],
)
def test_get_coin_combination_errors(bad_input: object) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(bad_input)

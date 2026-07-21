import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(
            0,
            [0] * 4,
            id="should return [0, 0, 0, 0] for 0 cents",
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return [1, 0, 0, 0] for 1 cent",
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="should return [0, 1, 0, 0] for 5 cents",
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="should return [0, 0, 1, 0] for 10 cents",
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="should return [0, 0, 0, 1] for 25 cents",
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return [1, 1, 1, 1] for 41 cents",
        ),
    ],
)
def test_get_coin_combination(cents: int, expected_result: list[int]) -> None:
    assert get_coin_combination(cents) == expected_result

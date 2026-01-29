import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="Should return correct value for 1 cent"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="Should return correct value for 6 cents"
        ),
        pytest.param(
            18, [3, 1, 1, 0],
            id="Should return correct value for 18 cents"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="Should return correct value for 50 cents"
        ),
    ],
)
def test_should_return_correct_values(
        cents: int, result: list[int]
) -> None:
    assert get_coin_combination(cents) == result

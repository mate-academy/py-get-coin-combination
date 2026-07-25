import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="Should return zeros for 0 cents"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="Should return zeros for 0 cents"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="Should return zeros for 0 cents"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="Should return zeros for 0 cents"
        )
    ]
)
def test_should_return_result_correctly(
        cents: int,
        result: list[int]
) -> None:
    assert (
        get_coin_combination(cents) == result
    ), f"For {cents} cents result should be equal to {result}"

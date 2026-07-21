import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="some_text"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="some_text"
        ),
        pytest.param(
            5, [0, 1, 0, 0],
            id="some_text"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="some_text"
        ),
        pytest.param(
            10, [0, 0, 1, 0],
            id="some_text"
        ),
        pytest.param(
            11, [1, 0, 1, 0],
            id="some_text"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="some_text"
        ),
        pytest.param(
            113, [3, 0, 1, 4],
            id="some_text"
        ),
    ]
)
def test_get_coin_combination(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result

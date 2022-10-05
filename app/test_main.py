from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "_input, expected",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="For 'playgrounds' expected True"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="For '' expected True"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="For 'look' expected False"
        ),
        pytest.param(
            50, [0, 0, 0, 2],
            id="For 'Adam' expected False"
        )
    ],
)
def test_isogram(_input: str, expected: bool) -> None:
    assert get_coin_combination(_input) == expected

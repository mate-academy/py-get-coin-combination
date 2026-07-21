import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="returns all zeros if cents equal 0"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="returns 1 in the penny position if cents equal 1"
        ),
        pytest.param(
            41, [1, 1, 1, 1],
            id="returns ones in all positions if cents 41"
        ),
        pytest.param(
            216, [1, 1, 1, 8],
            id="returns all ones except quarters, because there are 8 of them"
        )
    ]
)
def test_coin_combination(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result

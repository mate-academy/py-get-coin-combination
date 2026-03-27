import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should add value to 0 index element"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should add value to 0 and 1 index element"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should add value to 0, 1 and 2 index element"
        ),
        pytest.param(
            66,
            [1, 1, 1, 2],
            id="should add value to 0, 1, 2 and 3 index element"
        )
    ],
)
def test_check_right_answers(
        cents: int,
        expected_result: list
) -> None:
    assert get_coin_combination(cents) == expected_result

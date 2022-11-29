import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "test_cents, test_result",
    [
        pytest.param(
            7, [2, 1, 0, 0],
            id="result_have_to_be_correct"
        ),
        pytest.param(
            33, [3, 1, 0, 1],
            id="result_have_to_be_correct"
        ),
        pytest.param(
            0, [0, 0, 0, 0],
            id="result_have_to_be_correct"
        ),
    ]
)
def test_result_have_to_be_correct(test_cents: int,
                                   test_result: list) -> None:
    assert get_coin_combination(test_cents) == test_result

import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            1, [1, 0, 0, 0], id="test_sould_return_correct_result_1"),
        pytest.param(
            6, [1, 1, 0, 0], id="test_sould_return_correct_result_2"),
        pytest.param(
            17, [2, 1, 1, 0], id="test_sould_return_correct_result_3"),
        pytest.param(
            50, [0, 0, 0, 2], id="test_sould_return_correct_result_4")
    ]
)
def test_sould_return_correct_result(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result

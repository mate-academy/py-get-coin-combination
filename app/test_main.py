import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_three_params_are_passed(cents, combination):
    assert get_coin_combination(cents) == combination, (
        f"Function 'get_coin_combination' should return '{combination}' "
        f"when 'cents' is equal to {cents}"
    )
import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "common_sum,expected_result",
    [
        (0, [0, 0, 0, 0]),
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (67, [2, 1, 1, 2]),
    ],
    ids=[
        "0 common sum should be convert to [0, 0, 0, 0]",
        "1 common sum should be convert to 1 penny [1, 0, 0, 0]",
        "6 common sum should be convert to 1 penny and 1 nickel [1, 1, 0, 0]",
        "17 common sum should be convert "
        "to 2 penny and 1 nickel and 1 dimes [2, 1, 1, 0]",
        "50 common sum should be convert to 2 quarters [0, 0, 0, 2]",
        "67 common sum should be convert "
        "to 2 penny and 1 nickel and 1 dimes "
        "and 2 quarters [2, 1, 1, 2]",
    ],
)
def test_get_coin_combination(
    common_sum: int,
    expected_result: list[int],
) -> None:
    assert get_coin_combination(common_sum) == expected_result

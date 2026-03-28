import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "given, expected",
    [
        pytest.param(4, [4, 0, 0, 0],
                     id="should be only pennies"),
        pytest.param(6, [1, 1, 0, 0],
                     id="should be only pennies and nickels"),
        pytest.param(15, [0, 1, 1, 0],
                     id="should be only nickels and dimes"),
        pytest.param(25, [0, 0, 0, 1],
                     id="should be only quarters"),
        pytest.param(26, [1, 0, 0, 1],
                     id="should be only pennies and quarters"),
        pytest.param(30, [0, 1, 0, 1],
                     id="should be only nickels and quarters"),
        pytest.param(35, [0, 0, 1, 1],
                     id="should be only dimes and quarters"),
        pytest.param(36, [1, 0, 1, 1],
                     id="should be only pennies, dimes and quarters"),
        pytest.param(41, [1, 1, 1, 1],
                     id="everything should be"),
    ]
)
def test_checking_the_correct_result(given: int, expected: list) -> None:
    assert get_coin_combination(given) == expected

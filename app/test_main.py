from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents,expected_error",
    [
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return 1 pennie equael 1 cent"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return if 6 equael to (1 pennie + 1 nickel coin)"
        ),
        pytest.param(
            17, [2, 1, 1, 0],
            id="should return if 17 equael to (2 pennie + 1 nickel + 1 dime)"
        ),
        pytest.param(
            25, [0, 0, 0, 1],
            id="should return if 25 equael to 1 quarters"
        )
    ]
)
def test_should_return_expected_error(cents, expected_error):
    assert get_coin_combination(cents) == expected_error

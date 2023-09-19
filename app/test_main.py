import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "amount, expected",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="test if 'cents' is 0"
        ),
        pytest.param(
            4,
            [4, 0, 0, 0],
            id="test if 'cents' is 4 or less"
        ),
        pytest.param(
            5,
            [0, 1, 0, 0],
            id="test if 'cents' is 5"
        ),
        pytest.param(
            9,
            [4, 1, 0, 0],
            id="test if 'cents' is 9 or less"
        ),
        pytest.param(
            10,
            [0, 0, 1, 0],
            id="test if 'cents' is 10"
        ),
        pytest.param(
            19,
            [4, 1, 1, 0],
            id="test if 'cents' is 24 or less"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="test if 'cents' is 25"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="test if 'cents' more then 25"
        )
    ]
)
def test_get_coin_combination(amount, expected) -> int:
    assert get_coin_combination(amount) == expected

@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(
            None,
            TypeError,
            id="should raise 'TypeError' when 'cents' is 'None'"
        ),
        pytest.param(
            [],
            TypeError,
            id="should raise 'TypeError' when 'cents' is not integer"
        )
    ]
)
def test_errors(cents, expected) -> None:
    with pytest.raises(expected):
        get_coin_combination(cents)

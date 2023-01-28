import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return 0 when cents equals 0"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return 1 penny when cents equals 1 penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return 1 nickel when cents equals 1 nickel"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return 1 dime when cents equals 1 dime"
        ),
        pytest.param(
            25,
            [0, 0, 0, 1],
            id="should return 1 quarter when cents equals 1 quarter"
        )
    ]
)
def test_returns_correct_result(cents: int, result: list) -> None:
    assert get_coin_combination(cents) == result


def test_raises_typeerror_when_func_receives_incorrect_data() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("twenty")

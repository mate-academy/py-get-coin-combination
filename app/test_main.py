import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return the wright result: [0, 0, 0, 0]"
        ),
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="should return the wright result: [1, 0, 0, 0]"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="should return the wright result: [1, 1, 0, 0]"
        ),
        pytest.param(
            16,
            [1, 1, 1, 0],
            id="should return the wright result: [1, 1, 1, 0]"
        ),
        pytest.param(
            41,
            [1, 1, 1, 1],
            id="should return the wright result: [1, 1, 1, 1]"
        ),
        pytest.param(
            100041,
            [1, 1, 1, 4001],
            id="should return the wright result: [1, 1, 1, 4001]"
        ),
    ]
)
def test_calculation_correctly(
        cents: int,
        result: list[int]
) -> None:
    assert get_coin_combination(cents) == result


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        pytest.param(
            "2",
            TypeError,
            id="should raise error if cents is string type"
        ),

    ]
)
def test_raising_error_correctly(
        cents: int | str,
        expected_error: Exception,
) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

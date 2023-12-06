import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "input_classes, expected_result",
    [
        pytest.param(
            3,
            [3, 0, 0, 0],
            id="should return correct list if input coins: 3"
        ),
        pytest.param(
            7,
            [2, 1, 0, 0],
            id="should return correct list if input coins: 7"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="should return correct list if input coins: 17"
        ),
        pytest.param(
            73,
            [3, 0, 2, 2],
            id="should return correct list if input coins: 73"
        ),
        pytest.param(
            0,
            [0, 0, 0, 0],
            id="should return correct list if input coins: 0"
        )

    ]
)
def test_nest(input_classes, expected_result):

    result = get_coin_combination(input_classes)

    assert result == expected_result

import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected_result",
    [
        pytest.param(
            0, [0, 0, 0, 0],
            id="should return zeros when there is no any cent"
        ),
        pytest.param(
            1, [1, 0, 0, 0],
            id="should return [1, 0, 0, 0] when there is 1 cent"
        ),
        pytest.param(
            6, [1, 1, 0, 0],
            id="should return [1, 1, 0, 0] when there are 6 cents"
        ),
        pytest.param(
            18, [3, 1, 1, 0],
            id="should return [3, 1, 1, 0] when there are 18 cents"
        ),
        pytest.param(
            44, [4, 1, 1, 1],
            id="should return [4, 1, 1, 1] when there are 44 cents"
        ),
        pytest.param(
            100, [0, 0, 0, 4],
            id="should return [0, 0, 0, 4] when there are 100 cents"
        ),
        pytest.param(
            124, [4, 0, 2, 4],
            id="should return [4, 0, 2, 4] when there are 124 cents"
        ),
        pytest.param(
            1248, [3, 0, 2, 49],
            id="should return [3, 0, 2, 49] when there are 1248 cents"
        )
    ]
)
def test_return_combination_correctly(
    cents: int,
    expected_result: list[int]
) -> None:
    assert get_coin_combination(cents) == expected_result

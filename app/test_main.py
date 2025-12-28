import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(
            1,
            [1, 0, 0, 0],
            id="one penny"
        ),
        pytest.param(
            6,
            [1, 1, 0, 0],
            id="six cents"
        ),
        pytest.param(
            17,
            [2, 1, 1, 0],
            id="seventeen cents"
        ),
    ]
)
def test_modify_class(cents: int, result: list[int]) -> None:
    assert get_coin_combination(cents) == result

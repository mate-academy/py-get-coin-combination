import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, expected",
    [
        (44, [4, 1, 1, 1]),
        (66, [1, 1, 1, 2]),
        (118, [3, 1, 1, 4]),
    ]
)
def test_should_return_every_coin(cents, expected):
    assert get_coin_combination(cents) == expected, (
        f'Function "get_coin_combination" should return {expected} '
        f'when "cents" equals to {cents}'
    )


def test_should_return_min_coin_amount():
    assert get_coin_combination(41) == [1, 1, 1, 1], (
        "Function 'test_should_return_min_coin_amount' should return min "
        "possible coin combination"
    )


@pytest.mark.parametrize(
    "cents, expected",
    [
        pytest.param(1, [1, 0, 0, 0], id="should return 1 penny"),
        pytest.param(5, [0, 1, 0, 0], id="should return 1 nickel"),
        pytest.param(10, [0, 0, 1, 0], id="should return 1 dim"),
        pytest.param(25, [0, 0, 0, 1], id="should return 1 quarter"),
        pytest.param(6, [1, 1, 0, 0], id="should return 1 penny and 1 nickel"),
        pytest.param(26, [1, 0, 0, 1], id="should be 1 penny and 1 quarter"),
        pytest.param(50, [0, 0, 0, 2], id="should return 2 quarters")
    ]
)
def test_should_return_coin_with_zeros(cents, expected):
    assert get_coin_combination(cents) == expected

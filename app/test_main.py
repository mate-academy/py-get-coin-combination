import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
        (0, [0, 0, 0, 0])
    ]
)
def test_should_return_right_values(cents: int, result: list) -> None:
    assert (
        get_coin_combination(cents) == result
    )


@pytest.mark.parametrize(
    "cents",
    [
        "a",
        [],
    ],
    ids=[
        "if input are string",
        "if input are list",
    ]
)
def test_should_raise_error(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)

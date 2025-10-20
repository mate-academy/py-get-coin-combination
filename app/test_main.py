import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cent, expected", [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (42, [2, 1, 1, 1]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_get_coin_combination(cent: int, expected: list[int]) -> None:
    assert get_coin_combination(cent) == expected


def test_get_coin_combination_get_error_if_cents_negative() -> None:
    with pytest.raises(ValueError):
        get_coin_combination(-1)


def test_get_coin_combination_get_error_if_cents_none() -> None:
    with pytest.raises(TypeError):
        get_coin_combination(None)

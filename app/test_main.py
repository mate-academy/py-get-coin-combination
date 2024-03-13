import pytest
from typing import Type

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (
            cents,
            [
                cents % 5,
                ((cents % 25) % 10) // 5,
                (cents % 25) // 10,
                cents // 25
            ]
        ) for cents in range(0, 100 + 1)
    ],
)
def test_normal_values(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents=cents) == expected_result


@pytest.mark.parametrize(
    "cents,expected_result",
    [
        (
            cents,
            [
                cents % 5,
                ((cents % 25) % 10) // 5,
                (cents % 25) // 10,
                cents // 25
            ]
        ) for cents in range(1_000, 100_000_000_000, 987_654_321)
    ],
)
def test_large_values(cents: int, expected_result: list) -> None:
    assert get_coin_combination(cents=cents) == expected_result


@pytest.mark.parametrize(
    "cents",
    [
        None,
        "",
        [],
        dict(),
        set(),
    ],
)
def test_argument_types(
        cents: int,
        expected_error: Type[Exception] = TypeError
) -> None:
    with pytest.raises(TypeError):
        assert get_coin_combination(cents=cents) == expected_error

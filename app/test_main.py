import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize("cents, expected", [
    (1, [1, 0, 0, 0]),
    (6, [1, 1, 0, 0]),
    (17, [2, 1, 1, 0]),
    (50, [0, 0, 0, 2])
]
)
def test_for_getting_correct_coin_combination(cents: int,
                                              expected: list) -> None:
    assert get_coin_combination(cents) == expected


@pytest.mark.parametrize(
    "cents, expected_error",
    [
        ("1", TypeError)
    ],
    ids=[
        "Cents should be an integer"
    ]
)
def test_raise_exception_correctly(cents: int,
                                   expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_coin_combination(cents)

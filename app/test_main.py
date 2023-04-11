import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,result",
    [
        (0, [0, 0, 0, 0]),
        (4, [4, 0, 0, 0]),
        (9, [4, 1, 0, 0]),
        (19, [4, 1, 1, 0]),
        (244, [4, 1, 1, 9]),
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ]
)
def tests_checks_all_edged_situations(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result


def test_incorrect_type_of_data() -> None:
    with pytest.raises(TypeError):
        get_coin_combination("28")

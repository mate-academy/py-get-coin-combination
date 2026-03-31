import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "penni_count,result_combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_must_calculate_values_correctly(
    penni_count: int,
    result_combination: list
) -> None:
    assert get_coin_combination(penni_count) == result_combination


@pytest.mark.parametrize(
    "penni_count",
    [
        (-1,),
        ("6",),
        (None,),
        (True,)
    ]
)
def test_must_raise_error_when_incorrect_argument(
    penni_count: int
) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(penni_count)

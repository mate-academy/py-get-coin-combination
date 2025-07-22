from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    ("cents"),
    [
        pytest.param("1", id="TypeError if string"),
        pytest.param(None, id="TypeError if None"),
    ]
)
def test_should_raise_error_if_incorrect_value(cents: int) -> None:
    with pytest.raises(TypeError):
        get_coin_combination(cents)


@pytest.mark.parametrize(
    ("cents,result"),
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2]),
    ]
)
def test_should_calculate_correctly_if_correct_input(
        cents: int,
        result: list
) -> None:
    assert get_coin_combination(cents) == result


if __name__ == "__main__":
    pass
